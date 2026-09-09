#!/usr/bin/env python3
"""Refresh a project's development links, optionally fast-forwarding the source."""

import argparse
import json
import os
from pathlib import Path
import subprocess
import sys


SOURCE_ROOT = Path(__file__).resolve().parents[3]


def run(command):
    result = subprocess.run(command, text=True, capture_output=True, timeout=60)
    if result.returncode:
        raise ValueError(result.stderr.strip() or result.stdout.strip() or "Command failed")
    return result.stdout.strip()


def git(source, *arguments):
    return run(["git", "-C", str(source), *arguments])


def source_info(source):
    try:
        top = Path(git(source, "rev-parse", "--show-toplevel")).resolve()
        if top != source:
            return {"revision": None, "branch": None, "local_edits": None}
        revision = git(source, "rev-parse", "HEAD")
        branch = git(source, "rev-parse", "--abbrev-ref", "HEAD")
        edits = git(source, "status", "--short", "--untracked-files=all")
        return {"revision": revision, "branch": branch, "local_edits": edits}
    except (OSError, ValueError):
        return {"revision": None, "branch": None, "local_edits": None}


def check_links(project, source, harness):
    """A refresh may add links, but converting existing copies is installer work."""
    for skill in sorted((source / "skills").glob("*/SKILL.md")):
        canonical = project / ".agents" / "skills" / skill.parent.name
        entries = [(canonical, skill.parent)]
        if harness == "both":
            entries.append((project / ".claude" / "skills" / skill.parent.name, canonical))
        for link, target in entries:
            for parent in link.parents:
                if parent == project:
                    break
                if parent.is_symlink() or (parent.exists() and not parent.is_dir()):
                    raise ValueError(f"Invalid development install parent: {parent}")
            if not (link.exists() or link.is_symlink()):
                continue
            if (not link.is_symlink()
                    or Path(os.path.abspath(link.parent / link.readlink())) != target):
                raise ValueError(f"Conflicting installed skill: {link}. Use the source installer "
                                 "with --dev to deliberately back up and convert it.")


def refresh(project, pull=False):
    project = Path(project).expanduser().resolve()
    source = SOURCE_ROOT.resolve()
    canonical = project / ".agents" / "skills" / "campaign-refresh"
    installer = source / "scripts" / "install.py"
    if (not canonical.is_symlink()
            or canonical.resolve() != source / "skills" / "campaign-refresh"
            or not installer.is_file()):
        raise ValueError("This helper needs a development installation. Run the source "
                         "checkout's scripts/install.py with --dev first. "
                         "Copied skills and plugin caches are not source checkouts.")
    # Do not follow a relocated/symlinked installation parent into another project.
    for parent in canonical.parents:
        if parent == project:
            break
        if parent.is_symlink():
            raise ValueError(f"Refusing a symlinked install directory: {parent}")

    alias = project / ".claude" / "skills" / "campaign-refresh"
    harness = "both" if alias.exists() or alias.is_symlink() else "codex"
    check_links(project, source, harness)
    before = source_info(source)
    pull_output = None
    changed = []
    if pull:
        if before["revision"] is None:
            raise ValueError("The development source is not the root of a Git checkout.")
        if before["local_edits"]:
            raise ValueError("The development source has local changes; use a local refresh "
                             "or commit them in the source checkout before pulling.")
        if before["branch"] == "HEAD":
            raise ValueError("The development source has a detached HEAD; choose its branch first.")
        upstream = git(source, "rev-parse", "--abbrev-ref", "--symbolic-full-name", "@{upstream}")
        pull_output = git(source, "pull", "--ff-only", "--no-rebase", "--no-autostash")
        changed = git(source, "diff", "--name-only", before["revision"], "HEAD", "--", "skills").splitlines()
    else:
        upstream = None

    # Execute the current installer after pulling, so newly introduced skills get links.
    try:
        check_links(project, source, harness)
        install_output = run([sys.executable, str(installer), "--project", str(project),
                              "--harness", harness, "--dev"])
    except (OSError, ValueError, subprocess.TimeoutExpired) as error:
        if pull_output is not None:
            raise ValueError(f"Source pull succeeded, but project link refresh failed: {error}") from error
        raise
    after = source_info(source)
    return {
        "source": str(source),
        "project": str(project),
        **after,
        "previous_revision": before["revision"],
        "upstream": upstream,
        "pull_output": pull_output,
        "changed_by_pull": changed,
        "installation": install_output,
        "reread": [str(source / "skills" / "campaign-refresh" / "SKILL.md"),
                   str(source / "skills" / "campaign-start" / "references" / "campaign-workflow-overview.md")],
        "next": "Reread these files and the skill for the current action before continuing.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", required=True, type=Path)
    parser.add_argument("--pull", action="store_true",
                        help="Fast-forward the clean development source from its configured upstream.")
    args = parser.parse_args()
    try:
        result = refresh(args.project, pull=args.pull)
    except (OSError, ValueError, subprocess.TimeoutExpired) as error:
        parser.exit(1, f"Refresh failed: {error}\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
