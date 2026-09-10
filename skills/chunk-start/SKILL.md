---
name: chunk-start
description: Begin implementing or investigating a campaign chunk, using current state, the intended plan, and selectively retrieved evidence.
---

# Start a chunk

Use `YYYY-MM-DD HH:mm ±HH:MM` for every new date stamp this skill records. Follow
[the shared timestamp convention](../campaign-start/references/campaign-workflow-overview.md#timestamps)
for filenames, time zones, and preserving historical records.

Identify the campaign and chunk from the request and current context. If ambiguous,
ask which one; do not pick between plausible campaigns silently. Read `STATE.md`
and the relevant spec/plan sections. Follow [record access](../campaign-start/references/record-access.md)
for applicable decisions/evidence, historical searches, or an older campaign without
state. Preserve valid approvals and active restrictions; adapt records only as needed
within this authorized update. Existing campaign locations and headings are fine.

Check the actual working state, recent changes, available inputs, and relevant
dependencies. Do not reset or stash unrelated work to create a clean starting point.
Reuse the working branch or worktree; arrange an appropriate working branch before
campaign commits. If this is an existing in-progress chunk, continue it.

Briefly state the intended outcome and how it will be assessed, mark it in progress
with its start timestamp in `STATE.md`, and **begin the work**. This is an execution
skill, not only an orientation.
Ask about missing information that materially changes the work while continuing
independent tasks already authorized.

Keep each chunk small enough for one session, including focused checks, review,
and documentation. Execute only the selected chunk. Revise `PLAN.md` only when
intended work changes; split or defer work when needed. Keep progress and the next
action in `STATE.md`. Record significant design/experimental choices in `DECISIONS.md`;
routine approvals or run events need no entry. Keep useful evidence in one note per
coherent activity. Make focused checkpoint commits at useful recovery points.

For experiments, run or help the user run the work according to their request and
resource constraints; there is no human-only execution rule. Record commands/configs,
code state including relevant uncommitted changes, input versions, material environment
details, and output locations in a run note. Distinguish observed results from
interpretation and disclose missing provenance.

Run checks appropriate to what changed. When the chunk's outcome is ready to assess,
suggest [chunk-review](../chunk-review/SKILL.md) before
[chunk-complete](../chunk-complete/SKILL.md) or marking the chunk complete, unless
an existing review covers the current work. If review is part of the current request,
run it; otherwise refresh the `STATE.md` handoff naming the campaign and chunk and
asking for `chunk-review` first, followed by `chunk-complete` after review and any
blocking findings are resolved. Keep the chunk open while review or blocking findings
remain unresolved.

If chunk completion is part of the request and the work is ready to close, use
`chunk-complete` and honor its stop and fresh-session handoff; do not advance
automatically to another chunk. For workflow questions, consult
[the overview](../campaign-start/references/campaign-workflow-overview.md).
