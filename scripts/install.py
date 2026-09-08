#!/usr/bin/env python3
"""Copy the shared skills into a project's harness discovery directories."""

import argparse
from pathlib import Path
import shutil


def install(project, harness):
    project = Path(project).expanduser().resolve()
    if not project.is_dir():
        raise ValueError(f"Project directory does not exist: {project}")
    source = Path(__file__).resolve().parents[1] / "skills"
    skills = sorted(path.parent for path in source.glob("*/SKILL.md"))
    if not skills:
        raise ValueError(f"No skills found in {source}")
    roots = {
        "codex": [".agents"],
        "claude": [".claude"],
        "both": [".agents", ".claude"],
    }[harness]
    copies = [(skill, project / root / "skills" / skill.name)
              for root in roots for skill in skills]

    # Check every destination before writing either harness's files.
    for _, destination in copies:
        for parent in destination.parents:
            if parent == project:
                break
            if parent.is_symlink():
                raise ValueError(f"Refusing a symlinked install directory: {parent}")
            if parent.exists() and not parent.is_dir():
                raise ValueError(f"Install parent is not a directory: {parent}")
        if destination.exists() or destination.is_symlink():
            raise ValueError(f"Already exists; back up before replacing: {destination}")

    for skill, destination in copies:
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(skill, destination,
                        ignore=shutil.ignore_patterns(".DS_Store", "__pycache__", "*.pyc"))
    return [destination for _, destination in copies]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", required=True, type=Path)
    parser.add_argument("--harness", required=True, choices=("codex", "claude", "both"))
    args = parser.parse_args()
    try:
        destinations = install(args.project, args.harness)
    except (OSError, ValueError) as error:
        parser.exit(1, f"Install failed: {error}\n")
    print(f"Installed {len(destinations)} skill directories:")
    for destination in destinations:
        print(destination)


if __name__ == "__main__":
    main()
