#!/usr/bin/env python3
"""Install shared campaign skills, or link projects to a development checkout."""

import argparse
import os
from pathlib import Path
import shutil
import tempfile


SOURCE = Path(__file__).resolve().parents[1] / "skills"


def check_parents(destination, project):
    for parent in destination.parents:
        if parent == project:
            break
        if parent.is_symlink():
            raise ValueError(f"Refusing a symlinked install directory: {parent}")
        if parent.exists() and not parent.is_dir():
            raise ValueError(f"Install parent is not a directory: {parent}")


def points_to(link, target):
    """Compare link destinations without following another skill's symlink."""
    return (link.is_symlink()
            and Path(os.path.abspath(link.parent / link.readlink())) == target)


def install_dev(project, copies, links, source):
    # Development links are absolute so moving the consuming project is harmless.
    # Claude links still point at the project's canonical .agents entries.
    desired = copies + links
    changes = []
    for target, destination in desired:
        if points_to(destination, target):
            continue
        if destination.exists() and not destination.is_symlink():
            if not destination.is_dir() or not (destination / "SKILL.md").is_file():
                raise ValueError(f"Not an installed skill; leaving it alone: {destination}")
        changes.append((target, destination))

    # Retire only stale links into this exact development source. Unrelated skills,
    # including real directories with old skill names, are not ours to remove.
    names = {destination.name for _, destination in copies}
    shared = project / ".agents" / "skills"
    if shared.is_dir():
        for destination in sorted(shared.iterdir()):
            if destination.name in names or not points_to(destination, source / destination.name):
                continue
            changes.append((None, destination))
            alias = project / ".claude" / "skills" / destination.name
            if points_to(alias, destination):
                check_parents(alias, project)
                changes.append((None, alias))

    existing = [destination for _, destination in changes
                if destination.exists() or destination.is_symlink()]
    backup = None
    if existing:
        backup_root = project / ".agents" / "campaign-workflow-backups"
        check_parents(backup_root / "entry", project)
        backup_root.mkdir(parents=True, exist_ok=True)
        backup = Path(tempfile.mkdtemp(prefix="dev-", dir=backup_root))

    moved = []
    created = []
    try:
        for target, destination in changes:
            destination.parent.mkdir(parents=True, exist_ok=True)
            if destination.exists() or destination.is_symlink():
                saved = backup / destination.relative_to(project)
                saved.parent.mkdir(parents=True, exist_ok=True)
                destination.rename(saved)
                moved.append((saved, destination))
            if target is not None:
                link_target = (target if destination.parent == shared
                               else Path(os.path.relpath(target, destination.parent)))
                destination.symlink_to(link_target, target_is_directory=True)
                created.append(destination)
    except OSError:
        for destination in reversed(created):
            destination.unlink()
        for saved, destination in reversed(moved):
            saved.rename(destination)
        if backup is not None:
            shutil.rmtree(backup)
        raise

    if backup is not None:
        print(f"Preserved replaced entries in {backup}")
    return [destination for _, destination in desired]


def install(project, harness, dev=False):
    project = Path(project).expanduser().resolve()
    if not project.is_dir():
        raise ValueError(f"Project directory does not exist: {project}")
    if harness not in ("codex", "claude", "both"):
        raise ValueError(f"Unknown harness: {harness}")
    source = SOURCE.resolve()
    skills = sorted(path.parent for path in source.glob("*/SKILL.md"))
    if not skills:
        raise ValueError(f"No skills found in {source}")
    copies = [(skill, project / ".agents" / "skills" / skill.name)
              for skill in skills]
    links = ([(canonical, project / ".claude" / "skills" / skill.name)
              for skill, canonical in copies] if harness != "codex" else [])
    destinations = [destination for _, destination in copies + links]

    # Check every destination before changing either harness's installation.
    for destination in destinations:
        check_parents(destination, project)
        if not dev and (destination.exists() or destination.is_symlink()):
            raise ValueError(f"Already exists; back up before replacing: {destination}")

    if dev:
        return install_dev(project, copies, links, source)

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
    parser.add_argument("--dev", action="store_true",
                        help="Link to this checkout; back up existing skill copies or links first.")
    args = parser.parse_args()
    try:
        destinations = install(args.project, args.harness, dev=args.dev)
    except (OSError, ValueError) as error:
        parser.exit(1, f"Install failed: {error}\n")
    print(f"Installed {len(destinations)} skill directories or links:")
    for destination in destinations:
        if destination.is_symlink():
            print(f"{destination} -> {destination.readlink()}")
        else:
            print(destination)
    if args.dev:
        print("Development skills share this checkout, including uncommitted edits.")
        print("In an ongoing task, ask: Refresh campaign skills, then continue.")


if __name__ == "__main__":
    main()
