---
name: chunk-start
description: Begin implementing or investigating a campaign chunk, using the current spec, living plan, and relevant notes.
---

# Start a chunk

Identify the campaign and chunk from the request and current context. If ambiguous,
ask which one; do not pick between plausible campaigns silently. Read its `SPEC.md`,
the relevant part of `PLAN.md`, and decisions or notes that affect this work.
Existing campaign locations and headings are fine.

Check the actual working state, recent changes, available inputs, and relevant
dependencies. Do not reset or stash unrelated work to create a clean starting point.
Reuse the working branch or worktree; arrange an appropriate working branch before
campaign commits. If this is an existing in-progress chunk, continue it.

Briefly state the intended outcome and how it will be assessed, mark it in progress
in the plan, and **begin the work**. This is an execution skill, not only an orientation.
Ask about missing information that materially changes the work while continuing
independent tasks already authorized.

Keep chunks manageable within a session. Update the plan as the approach changes;
split or defer remaining work when needed, leaving a concrete next action.
Capture consequential choices in `DECISIONS.md`, and use `notes/` freely for useful
working context. Make focused checkpoint commits at useful recovery points.

For experiments, run or help the user run the work according to their request and
resource constraints; there is no human-only execution rule. Record commands/configs,
code state including relevant uncommitted changes, input versions, material environment
details, and output locations in a run note. Distinguish observed results from
interpretation and disclose missing provenance.

Run checks appropriate to what changed. When the chunk's outcome is ready to assess,
use [chunk-review](../chunk-review/SKILL.md) if review is part of the current request,
or leave a clear handoff for review. For workflow questions, consult
[the overview](../campaign-start/references/campaign-workflow-overview.md).
