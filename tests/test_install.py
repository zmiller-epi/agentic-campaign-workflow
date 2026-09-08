"""Installation behavior and resource portability; no model calls required."""

import importlib.util
from pathlib import Path
import re
import tempfile
import unittest

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

    def test_both_harnesses_receive_identical_complete_skills(self):
        for relative in ("AGENTS.md", "CLAUDE.md", ".claude/settings.json",
                         "docs/campaigns/existing/SPEC.md"):
            path = self.project / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("existing user content", encoding="utf-8")
        destinations = module.install(self.project, "both")
        source_files = [path for entry in (ROOT / "skills").glob("*/SKILL.md")
                        for path in entry.parent.rglob("*")
                        if path.name != ".DS_Store" and "__pycache__" not in path.parts
                        and path.suffix != ".pyc"]
        for root in (".agents", ".claude"):
            for source in source_files:
                if source.is_file():
                    target = self.project / root / "skills" / source.relative_to(ROOT / "skills")
                    self.assertEqual(source.read_bytes(), target.read_bytes())
        self.assertEqual(len(destinations), 2 * len(list((ROOT / "skills").glob("*/SKILL.md"))))
        for relative in ("AGENTS.md", "CLAUDE.md", ".claude/settings.json",
                         "docs/campaigns/existing/SPEC.md"):
            self.assertEqual((self.project / relative).read_text(), "existing user content")

    def test_single_harness_install(self):
        for harness, root, absent in (("codex", ".agents", ".claude"),
                                      ("claude", ".claude", ".agents")):
            with self.subTest(harness=harness):
                project = self.project / harness
                project.mkdir()
                module.install(project, harness)
                self.assertTrue((project / root / "skills/campaign-start/SKILL.md").is_file())
                self.assertFalse((project / absent).exists())

    def test_collision_in_second_harness_prevents_all_writes(self):
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
            module.install(self.project, "codex")
        self.assertEqual(skill.read_text(), "customized")

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

    def test_missing_project_is_not_created(self):
        missing = self.project / "missing"
        with self.assertRaisesRegex(ValueError, "does not exist"):
            module.install(missing, "codex")
        self.assertFalse(missing.exists())

    def test_installed_markdown_links_resolve_without_checkout(self):
        module.install(self.project, "both")
        for harness in (".agents", ".claude"):
            installed = self.project / harness / "skills"
            for document in installed.rglob("*.md"):
                for target in re.findall(r"\]\(([^)]+)\)", document.read_text()):
                    if "://" in target or target.startswith("#"):
                        continue
                    path = (document.parent / target.split("#", 1)[0]).resolve()
                    self.assertTrue(path.is_relative_to(installed.resolve()), (document, target))
                    self.assertTrue(path.exists(), (document, target))


if __name__ == "__main__":
    unittest.main()
