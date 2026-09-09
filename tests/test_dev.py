"""Development links, conversion recovery, and local-Git refresh integration."""

from contextlib import redirect_stdout
import importlib.util
import io
from pathlib import Path
import json
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


installer = load("dev_installer", ROOT / "scripts/install.py")
refresher = load("dev_refresher", ROOT / "skills/campaign-refresh/scripts/refresh.py")


class DevelopmentFixture(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name).resolve()
        self.source = self.base / "workflow source"
        shutil.copytree(ROOT / "skills", self.source / "skills",
                        ignore=shutil.ignore_patterns("__pycache__", "*.pyc", ".DS_Store"))
        (self.source / "scripts").mkdir()
        shutil.copy2(ROOT / "scripts/install.py", self.source / "scripts/install.py")
        self.project = self.base / "consuming project"
        self.project.mkdir()
        self.canonical = self.project / ".agents/skills/campaign-start"
        self.alias = self.project / ".claude/skills/campaign-start"
        self.record = self.project / "docs/campaigns/current/PLAN.md"
        self.record.parent.mkdir(parents=True)
        self.record.write_text("Approved plan and existing evidence")
        for target, attribute, value in ((installer, "SOURCE", self.source / "skills"),
                                         (refresher, "SOURCE_ROOT", self.source)):
            patch = mock.patch.object(target, attribute, value)
            patch.start()
            self.addCleanup(patch.stop)

    def install(self, dev=True, harness="both"):
        with redirect_stdout(io.StringIO()):
            return installer.install(self.project, harness, dev=dev)

    def assert_record_preserved(self):
        self.assertEqual(self.record.read_text(), "Approved plan and existing evidence")


class DevelopmentTests(DevelopmentFixture):
    def test_shared_source_edits_reach_both_projects_and_harnesses(self):
        self.install()
        second = self.base / "second project"
        second.mkdir()
        installer.install(second, "both", dev=True)
        self.assertTrue(self.canonical.readlink().is_absolute())
        self.assertFalse(self.alias.readlink().is_absolute())
        (self.source / "skills/campaign-start/SKILL.md").write_text("new local instructions")
        for project in (self.project, second):
            for harness in (".agents", ".claude"):
                self.assertEqual((project / harness / "skills/campaign-start/SKILL.md").read_text(),
                                 "new local instructions")
        self.assert_record_preserved()

    def test_single_harness_dev_layouts(self):
        for harness in ("codex", "claude"):
            with self.subTest(harness=harness):
                project = self.base / harness
                project.mkdir()
                installer.install(project, harness, dev=True)
                self.assertTrue((project / ".agents/skills/campaign-start").is_symlink())
                self.assertEqual((project / ".claude/skills/campaign-start").is_symlink(),
                                 harness == "claude")

    def test_conversion_preserves_distinct_customizations_and_is_idempotent(self):
        self.install(dev=False)
        (self.canonical / "SKILL.md").write_text("custom Codex instructions")
        self.alias.unlink()
        self.alias.mkdir()
        (self.alias / "SKILL.md").write_text("custom Claude instructions")
        unrelated = self.project / ".agents/skills/unrelated/SKILL.md"
        unrelated.parent.mkdir()
        unrelated.write_text("unrelated")
        self.install()
        backups = list((self.project / ".agents/campaign-workflow-backups").iterdir())
        self.assertEqual(len(backups), 1)
        saved = backups[0]
        self.assertEqual((saved / ".agents/skills/campaign-start/SKILL.md").read_text(),
                         "custom Codex instructions")
        self.assertEqual((saved / ".claude/skills/campaign-start/SKILL.md").read_text(),
                         "custom Claude instructions")
        inode = self.canonical.lstat().st_ino
        self.install()
        self.assertEqual(self.canonical.lstat().st_ino, inode)
        self.assertEqual(list((self.project / ".agents/campaign-workflow-backups").iterdir()), backups)
        self.assertEqual(unrelated.read_text(), "unrelated")
        self.assert_record_preserved()

    def test_conversion_failure_restores_copies_and_original_aliases(self):
        self.install(dev=False)
        (self.canonical / "SKILL.md").write_text("customized")
        original_link = self.alias.readlink()
        real_symlink = Path.symlink_to
        calls = []

        def fail_later(path, *args, **kwargs):
            calls.append(path)
            if len(calls) == 3:
                raise OSError("simulated symlink failure")
            return real_symlink(path, *args, **kwargs)

        with mock.patch.object(Path, "symlink_to", fail_later):
            with self.assertRaisesRegex(OSError, "simulated"):
                self.install()
        self.assertFalse(self.canonical.is_symlink())
        self.assertEqual((self.canonical / "SKILL.md").read_text(), "customized")
        self.assertEqual(self.alias.readlink(), original_link)
        for entry in (self.project / ".agents/skills").iterdir():
            self.assertFalse(entry.is_symlink())
        self.assertEqual(list((self.project / ".agents/campaign-workflow-backups").iterdir()), [])
        self.assert_record_preserved()

    def test_dev_file_collision_is_detected_before_conversion(self):
        self.install(dev=False)
        collision = self.project / ".claude/skills/chunk-start"
        collision.unlink()
        collision.write_text("not a skill")
        with self.assertRaisesRegex(ValueError, "Not an installed skill"):
            self.install()
        self.assertFalse(self.canonical.is_symlink())
        self.assertEqual(collision.read_text(), "not a skill")
        self.assertFalse((self.project / ".agents/campaign-workflow-backups").exists())

    def test_backup_directory_symlink_is_rejected(self):
        self.install(dev=False)
        outside = self.base / "outside"
        outside.mkdir()
        (self.project / ".agents/campaign-workflow-backups").symlink_to(outside)
        with self.assertRaisesRegex(ValueError, "symlinked"):
            self.install()
        self.assertFalse(self.canonical.is_symlink())
        self.assertEqual(list(outside.iterdir()), [])

    def test_new_skills_are_added_and_only_owned_stale_links_are_retired(self):
        self.install()
        shutil.rmtree(self.source / "skills/chunk-review")
        new = self.source / "skills/new-skill"
        new.mkdir()
        (new / "SKILL.md").write_text("new skill")
        unrelated = self.project / ".agents/skills/unrelated"
        unrelated.symlink_to(self.base / "elsewhere")
        self.install()
        for harness in (".agents", ".claude"):
            self.assertEqual((self.project / harness / "skills/new-skill/SKILL.md").read_text(), "new skill")
            self.assertFalse((self.project / harness / "skills/chunk-review").is_symlink())
        self.assertTrue(unrelated.is_symlink())
        backup = next((self.project / ".agents/campaign-workflow-backups").iterdir())
        self.assertTrue((backup / ".agents/skills/chunk-review").is_symlink())

    def test_project_move_keeps_dev_source_links_working(self):
        self.install()
        moved = self.project.with_name("moved project")
        self.project.rename(moved)
        self.assertEqual((moved / ".claude/skills/campaign-start").resolve(),
                         self.source / "skills/campaign-start")

    def test_dev_relative_references_resolve_inside_the_source(self):
        self.install()
        for source in (self.source / "skills").rglob("*.md"):
            for harness in (".agents", ".claude"):
                document = self.project / harness / "skills" / source.relative_to(self.source / "skills")
                for target in re.findall(r"\]\(([^)]+)\)", document.read_text()):
                    if "://" in target or target.startswith("#"):
                        continue
                    resolved = (document.parent / target.split("#", 1)[0]).resolve()
                    self.assertTrue(resolved.is_relative_to(self.source / "skills"), (document, target))
                    self.assertTrue(resolved.exists(), (document, target))

    def test_refresh_does_not_convert_an_existing_conflicting_skill(self):
        self.install()
        new = self.source / "skills/new-skill"
        new.mkdir()
        (new / "SKILL.md").write_text("upstream skill")
        conflicting = self.project / ".agents/skills/new-skill"
        conflicting.mkdir()
        (conflicting / "SKILL.md").write_text("unrelated local skill")
        with self.assertRaisesRegex(ValueError, "Conflicting installed skill"):
            refresher.refresh(self.project)
        self.assertEqual((conflicting / "SKILL.md").read_text(), "unrelated local skill")
        self.assertFalse((self.project / ".agents/campaign-workflow-backups").exists())

    def test_local_refresh_works_without_git_and_rejects_copied_installations(self):
        self.install(dev=False)
        with self.assertRaisesRegex(ValueError, "development installation"):
            refresher.refresh(self.project, pull=True)
        self.install()
        result = refresher.refresh(self.project)
        self.assertIsNone(result["revision"])
        self.assertEqual(result["source"], str(self.source))
        self.assertTrue(all(Path(path).is_file() for path in result["reread"]))
        with self.assertRaisesRegex(ValueError, "root of a Git checkout"):
            refresher.refresh(self.project, pull=True)
        self.assert_record_preserved()


class GitRefreshTests(DevelopmentFixture):
    def git(self, directory, *args):
        result = subprocess.run(["git", "-C", str(directory), *args],
                                text=True, capture_output=True, check=True)
        return result.stdout.strip()

    def init_git(self):
        self.git(self.source, "init", "-b", "main")
        self.git(self.source, "config", "user.name", "Test")
        self.git(self.source, "config", "user.email", "test@example.invalid")
        self.git(self.source, "add", ".")
        self.git(self.source, "commit", "-m", "Initial workflow")
        self.remote = self.base / "remote.git"
        self.remote.mkdir()
        self.git(self.remote, "init", "--bare", "--initial-branch=main")
        self.git(self.source, "remote", "add", "origin", str(self.remote))
        self.git(self.source, "push", "-u", "origin", "main")
        self.writer = self.base / "writer"
        self.git(self.base, "clone", str(self.remote), str(self.writer))
        self.git(self.writer, "config", "user.name", "Test")
        self.git(self.writer, "config", "user.email", "test@example.invalid")
        self.install()

    def publish(self):
        added = self.writer / "skills/new-skill"
        added.mkdir()
        (added / "SKILL.md").write_text("upstream instructions")
        (self.writer / "skills/campaign-start/SKILL.md").write_text("updated upstream start")
        self.git(self.writer, "add", ".")
        self.git(self.writer, "commit", "-m", "New workflow instructions")
        self.git(self.writer, "push")

    def test_pull_fast_forwards_source_and_links_new_skills_without_changing_project_git(self):
        self.init_git()
        self.git(self.project, "init", "-b", "project-work")
        self.git(self.project, "config", "user.name", "Test")
        self.git(self.project, "config", "user.email", "test@example.invalid")
        self.git(self.project, "add", ".")
        self.git(self.project, "commit", "-m", "Existing project")
        project_head = self.git(self.project, "rev-parse", "HEAD")
        before = self.git(self.source, "rev-parse", "HEAD")
        self.publish()
        result = refresher.refresh(self.project, pull=True)
        self.assertEqual(result["previous_revision"], before)
        self.assertEqual(result["revision"], self.git(self.writer, "rev-parse", "HEAD"))
        self.assertIn("skills/new-skill/SKILL.md", result["changed_by_pull"])
        self.assertEqual((self.project / ".claude/skills/new-skill/SKILL.md").read_text(),
                         "upstream instructions")
        self.assertEqual(self.git(self.project, "rev-parse", "HEAD"), project_head)
        self.assertEqual(self.git(self.project, "branch", "--show-current"), "project-work")
        self.assert_record_preserved()

    def test_local_refresh_does_not_pull_and_dirty_pull_preserves_edits(self):
        self.init_git()
        before = self.git(self.source, "rev-parse", "HEAD")
        self.publish()
        source_skill = self.source / "skills/campaign-start/SKILL.md"
        source_skill.write_text("uncommitted local experiment")
        result = refresher.refresh(self.project)
        self.assertEqual(result["revision"], before)
        self.assertIn("skills/campaign-start/SKILL.md", result["local_edits"])
        self.assertIsNone(result["pull_output"])
        with self.assertRaisesRegex(ValueError, "local changes"):
            refresher.refresh(self.project, pull=True)
        self.assertEqual(source_skill.read_text(), "uncommitted local experiment")
        self.assertEqual(self.git(self.source, "rev-parse", "HEAD"), before)
        self.assertEqual(self.git(self.source, "stash", "list"), "")

    def test_detached_and_missing_upstream_are_refused(self):
        self.init_git()
        before = self.git(self.source, "rev-parse", "HEAD")
        self.git(self.source, "checkout", "--detach")
        with self.assertRaisesRegex(ValueError, "detached"):
            refresher.refresh(self.project, pull=True)
        self.git(self.source, "checkout", "-b", "untracked-branch")
        with self.assertRaises(ValueError):
            refresher.refresh(self.project, pull=True)
        self.assertEqual(self.git(self.source, "rev-parse", "HEAD"), before)

    def test_diverged_source_is_not_merged_or_rebased(self):
        self.init_git()
        self.publish()
        (self.source / "local-note").write_text("local work")
        self.git(self.source, "add", "local-note")
        self.git(self.source, "commit", "-m", "Local change")
        before = self.git(self.source, "rev-parse", "HEAD")
        with self.assertRaises(ValueError):
            refresher.refresh(self.project, pull=True)
        self.assertEqual(self.git(self.source, "rev-parse", "HEAD"), before)
        self.assertEqual(self.git(self.source, "status", "--porcelain"), "")
        self.assertFalse((self.source / ".git/MERGE_HEAD").exists())

    def test_pulled_skill_name_collision_preserves_the_local_skill(self):
        self.init_git()
        conflicting = self.project / ".claude/skills/new-skill"
        conflicting.mkdir()
        (conflicting / "SKILL.md").write_text("unrelated local instructions")
        self.publish()
        with self.assertRaisesRegex(ValueError, "Source pull succeeded, but project link refresh failed"):
            refresher.refresh(self.project, pull=True)
        self.assertEqual((conflicting / "SKILL.md").read_text(), "unrelated local instructions")
        self.assertFalse((self.project / ".agents/skills/new-skill").exists())
        self.assertEqual(self.git(self.source, "rev-parse", "HEAD"),
                         self.git(self.writer, "rev-parse", "HEAD"))
        self.assert_record_preserved()

    def test_refresh_cli_resolves_source_through_project_symlink(self):
        self.init_git()
        command = [sys.executable, str(self.project / ".agents/skills/campaign-refresh/scripts/refresh.py"),
                   "--project", str(self.project)]
        result = subprocess.run(command, text=True, capture_output=True, check=True)
        self.assertEqual(json.loads(result.stdout)["source"], str(self.source))


if __name__ == "__main__":
    unittest.main()
