---
name: campaign-refresh
description: Reload updated campaign workflow skills during an existing task, optionally pulling their shared development checkout when the user asks for upstream updates.
---

# Refresh campaign skills

Use `YYYY-MM-DD HH:mm ±HH:MM` for every new date stamp this skill records. Follow
[the shared timestamp convention](../campaign-start/references/campaign-workflow-overview.md#timestamps)
for filenames, time zones, and preserving historical records.

Use when the user asks to refresh or reload campaign skills, or pull the latest
campaign workflow instructions. A plain refresh uses current local files, including
uncommitted edits. Pull only when the user requests upstream updates.

Locate this project's `.agents/skills/campaign-refresh` and resolve its symlink to
the source checkout. Read the files from disk again even if an older version was
loaded earlier in the conversation. Keep the consuming project as the campaign
workspace; the source checkout contains the shared instructions, not its campaigns.

For a development installation, run the bundled [refresh helper](scripts/refresh.py)
with the absolute project root (the directory containing `.agents`):

```bash
python3 "/absolute/project/.agents/skills/campaign-refresh/scripts/refresh.py" --project "/absolute/project"
```

Add `--pull` only for an upstream-update request. It fast-forwards the source's
currently checked-out branch from its configured upstream, normally `main`, and
resynchronizes the project's development links to include new skills. It refuses
to pull a dirty or detached checkout, or a branch without a configured upstream. Do not reset, stash, switch
branches, or touch the consuming project's Git history to make a pull succeed.
If the user requests `main` but the reported source branch tracks something else,
resolve that mismatch before pulling. A local refresh remains available if a pull
is blocked; explain which revision is available instead of claiming an update.

If this is a copied or plugin installation, reread its current installed files for
a local refresh. For upstream changes, explain that development links need a one-time
setup from the workflow source checkout with `python3 scripts/install.py --project <project>
--harness <harness> --dev`. If the source is unknown, ask for its location. Do not run
Git pulls in a plugin cache or the consuming project, or silently convert installation
routes. An older installation without this skill can use the same installer command.

After the helper completes, reread this skill, [the overview](../campaign-start/references/campaign-workflow-overview.md),
and the skill for the current action, such as [campaign-resume](../campaign-resume/SKILL.md)
or [chunk-start](../chunk-start/SKILL.md). Read any supporting files needed by that
action from the same updated source. The helper updates links and reports paths;
it does not itself reload instructions into the conversation.

Report the source path, revision and local edits when available, plus relevant
behavior changes you can establish from the files or the prior conversation. For a
pull, the helper reports changed skill files. Without a previous revision or loaded
text, describe the current rules without inventing a change history.

Preserve campaign records, completed work, and valid prior approvals. Refreshing
instructions does not restart the campaign, regenerate its documents from templates,
or authorize a new plan. Surface any consequential mismatch with the current plan;
obtain approval of material plan changes before executing them. When the user asks
to continue, resume the next authorized action using the refreshed instructions.

Rereading existing Markdown instructions works in the current task. Do not promise
that newly added skill names or plugin tools have appeared in the harness's catalog.
Read a needed skill by path if discovery is stale, or suggest a fresh task if the
harness requires it. Never claim an installed plugin has been upgraded by a local reread.
