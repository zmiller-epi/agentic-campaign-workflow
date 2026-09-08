---
name: chunk-complete
description: Close a finished campaign chunk, record evidence and decisions, update the living plan, checkpoint work, and run documentation cleanup.
---

# Complete a chunk

Resolve the campaign and chunk. Compare the current work with its outcome and
verification in `PLAN.md`, using relevant review reports and actual evidence.
Check that the evidence still covers the current changes. Run any missing focused
checks that are practical and authorized. Do not claim unperformed checks passed.

If an unresolved issue invalidates the chunk's outcome, keep it open and state the
next action. A changed objective may justify splitting or replanning the chunk;
make that change explicit rather than retroactively declaring success.

Record consequential decisions and their reasons in `DECISIONS.md`. Preserve useful
working or run notes, link review evidence, and carry follow-ups into `PLAN.md`.
Mark the chunk complete when its current outcome is supported. Routine chunk closure
within the user's request needs no extra approval ceremony.

Update affected project documentation when this chunk changes setup, usage, interfaces,
or methods. Use the
[repository documentation guide](../campaign-start/references/repository-documentation.md)
when deciding where information belongs. Keep the detailed decision history and
evidence in the campaign, and link to them from current guidance where useful.

Run [campaign-cleanup](../campaign-cleanup/SKILL.md), preferably in a subagent.
Give it the selected campaign path and documentation ownership only; it is not alone
in the workspace and must preserve others' edits. Avoid editing those same documents
until it returns. Wait for its result, inspect any edits, and address consequential
discrepancies without treating cosmetic gaps as blockers. Use the same pass locally
if delegation is unavailable.

Make a focused checkpoint commit on the working branch, including relevant work and
documentation. Inspect the staged diff so unrelated changes are not swept in.
No tag, merge, or branch deletion is part of chunk completion.

Tell the user what finished, what evidence supports it, and the next useful action.
Point to the review or notes and summarize any unresolved follow-ups.
See [the overview](../campaign-start/references/campaign-workflow-overview.md)
if shared conventions are unclear.
