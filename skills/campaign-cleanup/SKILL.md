---
name: campaign-cleanup
description: Tidy a selected campaign's documentation after chunk completion, before campaign closure, or when resuming stale work; surface meaningful discrepancies.
---

# Clean up a campaign

Read [the workflow overview](../campaign-start/references/campaign-workflow-overview.md)
and the selected campaign's spec, plan, decisions, result, and relevant notes.
Use current work, reviews, and the supplied context as evidence. Follow project
conventions and user preferences over template wording.

This skill can be handed directly to a subagent with the campaign path and permission
to edit that campaign's documentation. No registered custom agent is needed.
When delegated, you own only those documents. You are not alone in the workspace:
preserve others' work, reread before editing, and report conflicting concurrent
changes rather than overwriting them. Do not spawn another cleanup agent.

Look for things that would mislead the next reader: stale chunk state, an unclear
next action, decisions without their known reasons, findings with no disposition,
broken evidence links, misplaced notes, or contradictions between claims and evidence.
Correct straightforward clerical issues and make small evidence-backed updates.

Preserve useful content, historical findings, experiment records, and the user's
wording. Link superseded material rather than erasing it. Adapt missing or older
document shapes incrementally; do not migrate or rename whole campaigns merely
to match the current template. In particular, `RESULTS.md`, `NOTES.md`,
`REVIEW.md`, and `experiments/` may contain valuable existing records.

Flag consequential discrepancies for the parent or user. Do not invent evidence,
approval, decisions, or run history; do not change scientific interpretations, expand
scope, mark substantive work complete, or close a campaign. Formatting differences,
empty optional sections, and missing per-chunk tags are not workflow failures.

Keep stable project guidance in appropriate project documentation. Do not grow
`AGENTS.md` or `CLAUDE.md` with campaign history or process checklists.
This pass does not change implementation, run expensive experiments, commit, merge,
tag, delete branches, or modify harness settings.

Return a concise account of edits, unresolved questions, and the recommended next
action. Write a note in `notes/` only if the findings merit a durable record.
A clean pass can simply say that no meaningful documentation issues were found.
