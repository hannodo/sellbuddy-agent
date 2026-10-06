"""Offline tests; no real account, browser or messages."""
import json
import re
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from install import ROOT, install, public_files
from build_share import build


class PackageTests(unittest.TestCase):
    def test_both_installations_and_no_overwrite(self):
        with tempfile.TemporaryDirectory() as folder:
            project = Path(folder).resolve()
            destinations = install("both", project)
            for destination in destinations:
                self.assertTrue((destination / "SKILL.md").is_file())
                self.assertTrue((destination / "references/interview.md").is_file())
            with self.assertRaises(ValueError):
                install("both", project)

    def test_symlink_destination_rejected(self):
        with tempfile.TemporaryDirectory() as folder:
            project = Path(folder).resolve()
            (project / "elsewhere").mkdir()
            (project / ".agents").symlink_to(project / "elsewhere", target_is_directory=True)
            with self.assertRaises(ValueError):
                install("codex", project)
            self.assertEqual(list((project / "elsewhere").iterdir()), [])

    def test_zip_allowlist_and_no_overwrite(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder).resolve()
            (root / "safe.md").write_text("public", encoding="utf-8")
            (root / "private.json").write_text("NOT FOR SHARING", encoding="utf-8")
            (root / "share-manifest.json").write_text('["safe.md"]', encoding="utf-8")
            output = root / "share.zip"
            build(output, root)
            with zipfile.ZipFile(output) as archive:
                self.assertEqual(archive.namelist(), ["sellbuddy-agent/safe.md"])
            with self.assertRaises(FileExistsError):
                build(output, root)

    def test_manifest_rejects_traversal(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder).resolve()
            (root / "share-manifest.json").write_text('["../private.json"]', encoding="utf-8")
            with self.assertRaises(ValueError):
                list(public_files(root))

    def test_configuration_is_inactive(self):
        config = json.loads((ROOT / "skills/sellbuddy-agent/assets/config.example.json").read_text())
        self.assertFalse(config["setup_complete"])
        self.assertFalse(config["monitoring"]["enabled"])
        self.assertFalse(any(config["permissions"].values()))

    def test_local_markdown_links(self):
        for path in public_files():
            if path.suffix != ".md":
                continue
            source = ROOT / path
            for link in re.findall(r"\]\(([^)]+)\)", source.read_text(encoding="utf-8")):
                if "://" in link or link.startswith("#"):
                    continue
                self.assertTrue((source.parent / link).is_file(), f"{path}: {link}")

    def test_manifest_symlink_rejected(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder).resolve()
            (root / "private.txt").write_text("private", encoding="utf-8")
            (root / "safe.md").symlink_to(root / "private.txt")
            (root / "share-manifest.json").write_text('["safe.md"]', encoding="utf-8")
            with self.assertRaises(ValueError):
                list(public_files(root))


if __name__ == "__main__":
    unittest.main()
