#!/usr/bin/env python3
"""Install the explicitly listed public skill files into a local project."""
import argparse
import json
import shutil
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PREFIX = Path("skills/sellbuddy-agent")


def public_files(root=ROOT):
    entries = json.loads((root / "share-manifest.json").read_text(encoding="utf-8"))
    if not isinstance(entries, list) or len(entries) != len(set(entries)):
        raise ValueError("Invalid or duplicate manifest entries")
    for name in entries:
        path = Path(name)
        if path.is_absolute() or ".." in path.parts or path.as_posix() != name or "\\" in name:
            raise ValueError("Unsafe manifest entry")
        source = root / path
        if any(part.is_symlink() for part in [source, *source.parents] if part != root.parent):
            raise ValueError("Symlinks are not allowed in package paths")
        if not source.is_file():
            raise ValueError("Missing public file: " + name)
        yield path


def install(host, project, root=ROOT):
    raw_project = Path(project).absolute()
    if not raw_project.is_dir():
        raise ValueError("Project folder must already exist")
    if any(p.is_symlink() for p in [raw_project, *raw_project.parents]):
        raise ValueError("Project path must not contain symlinks")
    project = raw_project.resolve()
    hosts = ["codex", "claude"] if host == "both" else [host]
    destinations = [
        project / (".agents" if h == "codex" else ".claude") / "skills" / "sellbuddy-agent"
        for h in hosts
    ]
    for destination in destinations:
        for parent in [destination, *destination.parents]:
            if parent == project:
                break
            if parent.is_symlink():
                raise ValueError("Destination path must not contain symlinks")
            if parent.exists() and not parent.is_dir():
                raise ValueError("Destination parent is not a folder")
        if destination.exists():
            raise ValueError("Refusing to overwrite: " + str(destination))
    members = [p for p in public_files(root) if p.is_relative_to(PREFIX)]
    if not members:
        raise ValueError("No skill files in manifest")
    # Staging avoids exposing an incomplete skill during copying.
    with tempfile.TemporaryDirectory(prefix="verkaufsplattform-skill-") as staging:
        staged = Path(staging) / "sellbuddy-agent"
        staged.mkdir()
        for member in members:
            target = staged / member.relative_to(PREFIX)
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(root / member, target)
        for destination in destinations:
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copytree(staged, destination)
            print("Installed:", destination)
    return destinations


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--host", choices=["codex", "claude", "both"], required=True)
    parser.add_argument("--project", required=True, help="Existing private sales folder")
    args = parser.parse_args()
    try:
        install(args.host, args.project)
    except (ValueError, OSError) as error:
        parser.exit(1, str(error) + "\n")


if __name__ == "__main__":
    main()
