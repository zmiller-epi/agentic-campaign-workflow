---
name: campaign-cleanup
description: Tidy a selected campaign's documentation after chunk completion, before campaign closure, or when resuming stale work; surface meaningful discrepancies.
---

# Clean up a campaign

Use `YYYY-MM-DD HH:mm ±HH:MM` for every new date stamp this skill records. Follow
[the shared timestamp convention](../campaign-start/references/campaign-workflow-overview.md#timestamps)
for filenames, time zones, and preserving historical records.

Read [the workflow overview](../campaign-start/references/campaign-workflow-overview.md),
current state, and the supplied scope. For routine chunk cleanup, start with affected
record sections, changed links, and evidence needed to check them. If scope is missing,
use the current chunk, state pointers, and recent document changes to identify it.
Expand when contradictions, missing context, or broken references warrant it.

For closure, reconcile the outcome, completion criteria, dispositions, and evidence
across the campaign. Follow [record access](../campaign-start/references/record-access.md)
for selective lookup or legacy records; do not load the whole notes directory by
default. Use actual work and evidence, honoring project conventions and user preferences.

This skill can be handed directly to a subagent with the campaign path and permission
to edit that campaign's documentation. No registered custom agent is needed.
When delegated, you own only those documents. You are not alone in the workspace:
preserve others' work, reread before editing, and report conflicting concurrent
changes rather than overwriting them. Do not spawn another cleanup agent.

Look for things that would mislead the next reader: stale chunk state, an unclear
next action, decisions without their known reasons, findings with no disposition,
broken evidence links, misplaced notes, or contradictions between claims and evidence.
Correct straightforward clerical issues and make small evidence-backed updates.
Keep progress/approvals/handoffs in `STATE.md`, intended work in `PLAN.md`, and only
significant design/experimental choices in `DECISIONS.md`. A routine event does not
need a new decision or note. Leave correct records and their `Updated` stamps alone.

Preserve useful content, historical findings, experiment records, and the user's
wording. Replace stale state rather than accumulating snapshots; preserve unique
useful history in linked notes first. When adapting older shapes within documentation
ownership, follow the preservation and link-repair procedure in record access. Keep
substantive decisions in place; relocate misplaced history without losing its content
or timestamps. Do not migrate or rename whole campaigns merely to match templates. In particular, `RESULTS.md`, `NOTES.md`,
`REVIEW.md`, and `experiments/` may contain valuable existing records.

Flag consequential discrepancies for the parent or user. Do not invent evidence,
approval, decisions, or run history; do not change scientific interpretations, expand
scope, mark substantive work complete, or close a campaign. Formatting differences,
empty optional sections, and missing per-chunk tags are not workflow failures.

Read relevant project guides to spot guidance made stale by the campaign. Use the
[repository documentation guide](../repo-init/references/repository-documentation.md)
when deciding where lasting information belongs. With campaign-only ownership,
report needed repo-level changes to the parent; do not edit those project files.
Keep `AGENTS.md` and `CLAUDE.md` small and avoid duplicating campaign history there.
This pass does not change implementation, run expensive experiments, commit, merge,
tag, delete branches, or modify harness settings.

Return a concise account of edits, unresolved questions, and the recommended next
action. Write a note in `notes/` only if the findings merit a durable record.
A clean pass can simply say that no meaningful documentation issues were found.
