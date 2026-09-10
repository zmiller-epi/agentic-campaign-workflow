---
name: chunk-complete
description: Close a finished campaign chunk, record evidence, update and clean up documentation, checkpoint work, and hand off the next action to a fresh session.
---

# Complete a chunk

Use `YYYY-MM-DD HH:mm ±HH:MM` for every new date stamp this skill records. Follow
[the shared timestamp convention](../campaign-start/references/campaign-workflow-overview.md#timestamps)
for filenames, time zones, and preserving historical records.

Chunk completion ends the current working session. Finish verification and the
documentation handoff for this chunk; do not start another chunk as part of completion.

Resolve the campaign and chunk from `STATE.md` and the relevant plan section. Follow
[record access](../campaign-start/references/record-access.md) for evidence lookup or older
campaigns. Before marking it complete, suggest running
[chunk-review](../chunk-review/SKILL.md) if no existing review covers the current
work. Run it when review is part of the current request, or leave a clear handoff
for review. Keep the chunk open while that review or its blocking findings remain
unresolved.

Compare the current work with its outcome and verification in `PLAN.md`, using
relevant review reports and actual evidence.
Check that the evidence still covers the current changes. Run any missing focused
checks that are practical and authorized. Do not claim unperformed checks passed.

If an unresolved issue invalidates the chunk's outcome, keep it open and state the
next action. A changed objective may justify splitting or replanning the chunk;
make that change explicit rather than retroactively declaring success.

Record a decision only if a significant design/experimental choice occurred; routine
completion does not qualify. Preserve useful run/working evidence in notes. Mark the
chunk complete with its timestamp in `STATE.md` when its outcome is supported, and
link the applicable review and evidence there. Revise `PLAN.md` only if follow-ups
change intended work. Routine chunk closure needs no extra approval ceremony.

Update affected project documentation when this chunk changes setup, usage, interfaces,
or methods. Use the
[repository documentation guide](../repo-init/references/repository-documentation.md)
when deciding where information belongs. Keep the detailed decision history and
evidence in the campaign, and link to them from current guidance where useful.

Replace the current handoff in `STATE.md` with essential evidence pointers, unresolved
follow-ups, branch/worktree, and the next chunk or review/closure action. Retain valid
approvals and restrictions; preserve unique useful history in notes before replacing
its only copy. Make the first step concrete for a fresh session. Leave later chunks
planned in state and completed chunks' intended work intact in the plan.

Run [campaign-cleanup](../campaign-cleanup/SKILL.md), preferably in a subagent.
Give it the campaign path, current chunk, affected records/links, and documentation
ownership only; it is not alone in the workspace and must preserve others' edits.
Start cleanup with that scope, expanding when discrepancies warrant it. Avoid editing those same documents
until it returns. Wait for its result, inspect any edits, and address consequential
discrepancies without treating cosmetic gaps as blockers. Use the same pass locally
if delegation is unavailable.

Make a focused checkpoint commit on the working branch, including relevant work,
documentation, and the handoff. Inspect the staged diff so unrelated changes are not
swept in. No tag, merge, or branch deletion is part of chunk completion.

Tell the user what finished and what evidence supports it, linking state and
relevant review or notes. **Stop here; do not begin the next chunk or automatically
run campaign review or campaign completion.** Suggest clearing context or starting
a new session before continuing. Provide a ready-to-use prompt naming the campaign
path and next action, such as resuming a specific chunk or reviewing the campaign
after its final chunk. A suggested next action is a handoff, not an instruction to
execute it in this session. Do not clear context on the user's behalf.
See [the overview](../campaign-start/references/campaign-workflow-overview.md)
if shared conventions are unclear.
