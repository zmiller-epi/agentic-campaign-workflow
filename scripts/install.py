#!/usr/bin/env python3
"""Install shared skills in .agents and link Claude Code to the same files."""

import argparse
import os
from pathlib import Path
import shutil


def install(project, harness):
    project = Path(project).expanduser().resolve()
    if not project.is_dir():
        raise ValueError(f"Project directory does not exist: {project}")
    if harness not in ("codex", "claude", "both"):
        raise ValueError(f"Unknown harness: {harness}")
    source = Path(__file__).resolve().parents[1] / "skills"
    skills = sorted(path.parent for path in source.glob("*/SKILL.md"))
    if not skills:
        raise ValueError(f"No skills found in {source}")
    copies = [(skill, project / ".agents" / "skills" / skill.name)
              for skill in skills]
    links = ([(canonical, project / ".claude" / "skills" / skill.name)
              for skill, canonical in copies] if harness != "codex" else [])
    destinations = [destination for _, destination in copies + links]

    # Check all copies and links before writing either harness's files.
    for destination in destinations:
        for parent in destination.parents:
            if parent == project:
                break
            if parent.is_symlink():
                raise ValueError(f"Refusing a symlinked install directory: {parent}")
            if parent.exists() and not parent.is_dir():
                raise ValueError(f"Install parent is not a directory: {parent}")
        if destination.exists() or destination.is_symlink():
            raise ValueError(f"Already exists; back up before replacing: {destination}")

    created = []
    try:
        for skill, destination in copies:
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.mkdir()
            created.append(destination)
            shutil.copytree(skill, destination, dirs_exist_ok=True,
                            ignore=shutil.ignore_patterns(".DS_Store", "__pycache__", "*.pyc"))
        for canonical, destination in links:
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.symlink_to(os.path.relpath(canonical, destination.parent),
                                   target_is_directory=True)
            created.append(destination)
    except OSError:
        # In particular, do not leave half an install when symlinks are unavailable.
        for destination in reversed(created):
            if destination.is_symlink():
                destination.unlink()
            elif destination.is_dir():
                shutil.rmtree(destination)
        raise
    return destinations


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", required=True, type=Path)
    parser.add_argument("--harness", required=True, choices=("codex", "claude", "both"))
    args = parser.parse_args()
    try:
        destinations = install(args.project, args.harness)
    except (OSError, ValueError) as error:
        parser.exit(1, f"Install failed: {error}\n")
    print(f"Installed {len(destinations)} skill directories or links:")
    for destination in destinations:
        if destination.is_symlink():
            print(f"{destination} -> {destination.readlink()}")
        else:
            print(destination)


if __name__ == "__main__":
    main()
