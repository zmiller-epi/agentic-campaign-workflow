---
name: campaign-resume
description: Reorient the user to an existing campaign and continue its current work, or provide an orientation-only summary when requested.
---

# Resume a campaign

Use `YYYY-MM-DD HH:mm ±HH:MM` for every new date stamp this skill records. Follow
[the shared timestamp convention](../campaign-start/references/campaign-workflow-overview.md#timestamps)
for filenames, time zones, and preserving historical records.

Find the campaign from the request, conversation, or current working branch and files.
Look in the project's campaign locations, including older engineering/experiment
folders. If several candidates fit, show brief choices and ask which one.
Do not read every previous campaign in full or treat missing status fields as inactivity.

Read `SPEC.md`, the current and next parts of `PLAN.md`, relevant decisions,
and recent notes or results. Inspect the actual working state and recent changes
to distinguish recorded plans from work already done. Account for an in-progress
chunk or a pending review/closure approval.

Give the user a short orientation: purpose, what has happened, current work,
material uncertainty, and the next useful action. Link the most relevant records.
Fix obvious stale pointers; when the documents disagree in a consequential way,
state the discrepancy and investigate or ask rather than inventing history.

If substantial drift makes the handoff confusing, use
[campaign-cleanup](../campaign-cleanup/SKILL.md) with documentation-only ownership,
or perform its pass locally. Wait for it before editing the same records.

When the user asks to resume or continue, proceed with the next authorized action,
using [chunk-start](../chunk-start/SKILL.md) for implementation, investigation, or
unfinished chunk work. Do not stop solely to require another skill invocation.
Use the recorded handoff and reuse valid approval; a fresh session does not require
reapproving an unchanged plan. Honor the stop after campaign planning, chunk completion,
or campaign completion. Do not automatically invoke resume at one of those boundaries
or treat a broad request to continue as permission to chain through later chunks.
An orientation-only request ends with the summary. If a real decision or approval
is pending, explain it and continue independent work while waiting. Do not silently
reopen a completed or abandoned campaign.

For shared conventions, see
[the overview](../campaign-start/references/campaign-workflow-overview.md).
