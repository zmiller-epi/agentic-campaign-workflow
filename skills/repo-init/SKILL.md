---
name: repo-init
description: Set up or refresh a repository's project documentation and shared agent instructions for campaign and standalone work, without starting a campaign.
---

# Initialize repository documentation

Use concise, plain language in records and responses. Keep needed facts, reasons,
evidence, uncertainty, and next actions; omit filler and repeated context.

Use `YYYY-MM-DD HH:mm ±HH:MM` for every new date stamp this skill records. Follow
[the shared timestamp convention](../campaign-start/references/campaign-workflow-overview.md#timestamps)
for filenames, time zones, and preserving historical records.

Use this when the user wants to introduce the workflow to a fresh or existing
project, or deliberately revisit its repository-level documentation. Resolve the
project directory from the request and current context before editing.

Read the current README, agent instructions, and relevant project docs. Inspect
enough code and configuration to understand what the project does and how it is used.
Consult notes or campaigns for specific questions using
[record access](../campaign-start/references/record-access.md); do not load campaign
history as routine repository orientation. In an empty project, use the user's stated intent
and ask only the questions needed to write a useful starting point. Keep planned
behavior distinct from something already implemented or verified.

Read [the repository documentation guide](references/repository-documentation.md)
for the document roles. Use the
[workflow overview](../campaign-start/references/campaign-workflow-overview.md)
when campaign conventions need clarification.

Create or improve the smallest useful set of project docs from the available
evidence: usually README.md, a small AGENTS.md, and development guidance. Add
design, data, or methods documentation only when there is content worth explaining.
Follow useful existing names and locations. Link the guides from the README and
put only concise project-specific constraints and reading pointers in AGENTS.md.
Missing information can stay an explicit unknown; do not invent commands or
constraints to complete a template.

When shared instructions are appropriate, create a relative CLAUDE.md -> AGENTS.md
symlink if CLAUDE.md is absent. If both files exist, read and reconcile their distinct
content before changing how they are shared. Preserve Claude-specific instructions
in a regular CLAUDE.md with an @AGENTS.md import when needed. Leave an existing
working link or import in place. Inspect existing links, including broken or external
targets, before attempting a repair; do not blindly follow or replace them.

Introduce the project's campaign and standalone-note locations through brief
pointers, normally docs/campaigns/ and docs/notes/. Do not create empty campaign
records or a folder for every suggested document. Repository setup can finish
without opening a campaign, and small tasks can proceed directly.

Make targeted, additive changes on repeat runs. Preserve custom content, existing
campaign records, and appropriate links instead of regenerating the documentation.
There is no initialization marker to maintain and no mandatory completeness check.
Investigate discrepancies that matter; record unresolved setup work in a short
standalone note only when it is worth preserving.

Verify documentation links and any practical, inexpensive commands you added.
State what was actually checked and what remains unknown. Use the user's existing
Git workflow and an appropriate working branch for a focused checkpoint if Git is
available. Preserve unrelated changes. Setting up documentation does not by itself
authorize package installation, code scaffolding, permission changes, remote
repository creation, or publication.

Summarize what is now documented, unresolved choices, and where to begin. If the user
also asked to start a campaign, continue with [campaign-start](../campaign-start/SKILL.md)
using the context already gathered. Otherwise leave the project ready for either a
campaign or standalone work. Campaign-start does not require this skill to have run.
