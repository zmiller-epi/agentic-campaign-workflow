"""Installation behavior and resource portability; no model calls required."""

import importlib.util
from pathlib import Path
import re
import tempfile
import unittest
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("campaign_install", ROOT / "scripts/install.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class InstallTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.project = Path(self.temp.name) / "project with spaces"
        self.project.mkdir()

    def test_both_harnesses_share_complete_skills_and_preserve_project_files(self):
        for relative in ("AGENTS.md", "CLAUDE.md", ".claude/settings.json",
                         "docs/campaigns/existing/SPEC.md"):
            path = self.project / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("existing user content", encoding="utf-8")
        destinations = module.install(self.project, "both")
        entries = list((ROOT / "skills").glob("*/SKILL.md"))
        source_files = [path for entry in entries for path in entry.parent.rglob("*")
                        if path.name != ".DS_Store" and "__pycache__" not in path.parts
                        and path.suffix != ".pyc"]
        for root in (".agents", ".claude"):
            for source in source_files:
                if source.is_file():
                    target = self.project / root / "skills" / source.relative_to(ROOT / "skills")
                    self.assertEqual(source.read_bytes(), target.read_bytes())
        for entry in entries:
            canonical = self.project / ".agents/skills" / entry.parent.name
            alias = self.project / ".claude/skills" / entry.parent.name
            self.assertFalse(canonical.is_symlink())
            self.assertTrue(alias.is_symlink())
            self.assertEqual(alias.resolve(), canonical.resolve())
        self.assertEqual(len(destinations), 2 * len(entries))
        for relative in ("AGENTS.md", "CLAUDE.md", ".claude/settings.json",
                         "docs/campaigns/existing/SPEC.md"):
            self.assertEqual((self.project / relative).read_text(), "existing user content")

    def test_single_harness_install(self):
        for harness in ("codex", "claude"):
            with self.subTest(harness=harness):
                project = self.project / harness
                project.mkdir()
                module.install(project, harness)
                canonical = project / ".agents/skills/campaign-start"
                self.assertTrue((canonical / "SKILL.md").is_file())
                if harness == "claude":
                    alias = project / ".claude/skills/campaign-start"
                    self.assertTrue(alias.is_symlink())
                    self.assertEqual(alias.resolve(), canonical.resolve())
                else:
                    self.assertFalse((project / ".claude").exists())

    def test_each_skill_distributes_the_root_license(self):
        license_text = (ROOT / "LICENSE").read_bytes()
        skills = sorted((ROOT / "skills").glob("*/SKILL.md"))
        self.assertTrue(skills)
        for skill in skills:
            with self.subTest(source=skill.parent.name):
                self.assertEqual((skill.parent / "LICENSE").read_bytes(), license_text)
        for harness in ("codex", "claude", "both"):
            with self.subTest(harness=harness):
                project = self.project / harness
                project.mkdir()
                module.install(project, harness)
                roots = (".agents",) if harness == "codex" else (".agents", ".claude")
                for root in roots:
                    for skill in skills:
                        installed = project / root / "skills" / skill.parent.name / "LICENSE"
                        self.assertEqual(installed.read_bytes(), license_text, str(installed))

    def test_collision_in_claude_prevents_all_writes(self):
        existing = self.project / ".claude/skills/chunk-start"
        existing.mkdir(parents=True)
        (existing / "SKILL.md").write_text("customized")
        with self.assertRaisesRegex(ValueError, "Already exists"):
            module.install(self.project, "both")
        self.assertFalse((self.project / ".agents").exists())
        self.assertEqual((existing / "SKILL.md").read_text(), "customized")
        self.assertEqual(list(existing.parent.iterdir()), [existing])

    def test_reinstall_does_not_overwrite(self):
        module.install(self.project, "codex")
        skill = self.project / ".agents/skills/chunk-start/SKILL.md"
        skill.write_text("customized")
        with self.assertRaises(ValueError):
            module.install(self.project, "both")
        self.assertEqual(skill.read_text(), "customized")
        self.assertFalse((self.project / ".claude").exists())

    def test_file_in_install_parent_prevents_all_writes(self):
        (self.project / ".claude").write_text("user file")
        with self.assertRaisesRegex(ValueError, "not a directory"):
            module.install(self.project, "both")
        self.assertFalse((self.project / ".agents").exists())

    def test_symlinked_parent_is_not_followed(self):
        external = Path(self.temp.name) / "external"
        external.mkdir()
        (self.project / ".agents").symlink_to(external, target_is_directory=True)
        with self.assertRaisesRegex(ValueError, "symlinked"):
            module.install(self.project, "codex")
        self.assertEqual(list(external.iterdir()), [])

    def test_broken_claude_link_is_not_replaced(self):
        alias = self.project / ".claude/skills/chunk-start"
        alias.parent.mkdir(parents=True)
        alias.symlink_to("missing-target", target_is_directory=True)
        with self.assertRaisesRegex(ValueError, "Already exists"):
            module.install(self.project, "both")
        self.assertEqual(alias.readlink(), Path("missing-target"))
        self.assertFalse((self.project / ".agents").exists())

    def test_missing_project_is_not_created(self):
        missing = self.project / "missing"
        with self.assertRaisesRegex(ValueError, "does not exist"):
            module.install(missing, "codex")
        self.assertFalse(missing.exists())

    def test_links_share_edits_and_survive_project_move(self):
        module.install(self.project, "both")
        moved = self.project.with_name("moved project")
        self.project.rename(moved)
        canonical = moved / ".agents/skills/chunk-start/SKILL.md"
        alias = moved / ".claude/skills/chunk-start/SKILL.md"
        self.assertFalse(alias.parent.readlink().is_absolute())
        canonical.write_text("shared update")
        self.assertEqual(alias.read_text(), "shared update")
        alias.write_text("edit through Claude")
        self.assertEqual(canonical.read_text(), "edit through Claude")

    def test_symlink_failure_rolls_back_only_new_skills(self):
        unrelated = self.project / ".agents/skills/unrelated/SKILL.md"
        unrelated.parent.mkdir(parents=True)
        unrelated.write_text("user skill")
        with mock.patch.object(Path, "symlink_to", side_effect=OSError("symlinks unavailable")):
            with self.assertRaisesRegex(OSError, "symlinks unavailable"):
                module.install(self.project, "both")
        self.assertEqual(unrelated.read_text(), "user skill")
        self.assertEqual(list(unrelated.parent.parent.iterdir()), [unrelated.parent])
        self.assertEqual(list((self.project / ".claude/skills").iterdir()), [])

    def test_installed_markdown_links_resolve_through_each_harness(self):
        module.install(self.project, "both")
        shared = self.project / ".agents/skills"
        relative_documents = [path.relative_to(shared) for path in shared.rglob("*.md")]
        for harness in (".agents", ".claude"):
            # Walk the shared tree explicitly: pathlib.rglob does not follow directory links.
            for relative in relative_documents:
                document = self.project / harness / "skills" / relative
                for target in re.findall(r"\]\(([^)]+)\)", document.read_text()):
                    if "://" in target or target.startswith("#"):
                        continue
                    path = (document.parent / target.split("#", 1)[0]).resolve()
                    self.assertTrue(path.is_relative_to(shared.resolve()), (document, target))
                    self.assertTrue(path.exists(), (document, target))


if __name__ == "__main__":
    unittest.main()
