---
name: campaign-resume
description: Inspect an existing campaign, orient the user to its current state, and pause for the user to decide what to do next.
---

# Resume a campaign

This is an orientation step. Inspect the campaign and working state, explain what
is going on, and end the turn waiting for the user's next direction. A request to
resume does not itself authorize starting or continuing campaign work, even when
the recorded plan is approved or a chunk is already in progress.

Find the campaign from the request, conversation, or current working branch and files.
Look in the project's campaign locations, including older engineering/experiment
folders. If several candidates fit, show brief choices and ask which one.
Do not read every previous campaign in full or treat missing status fields as inactivity.

Read `SPEC.md`, the current and next parts of `PLAN.md`, relevant decisions,
and recent notes or results. Inspect the actual working state and recent changes
to distinguish recorded plans from work already done. Account for an in-progress
chunk or a pending review/closure approval.

Keep this inspection read-only. If records disagree, investigate enough to explain
the discrepancy without inventing history. Surface stale pointers and substantial
drift in the orientation; suggest [campaign-cleanup](../campaign-cleanup/SKILL.md)
when useful, leaving repairs for the user's decision.

Give the user a short orientation: purpose, what has happened, current work,
material uncertainty or pending decisions, and the next useful action. Link the
most relevant records. Distinguish a recommended next action from work already done.

**End with a concise question about what the user wants to do next, then stop.**
Do not start or continue a chunk, invoke review or cleanup, reopen a completed or
abandoned campaign, or perform independent campaign work while waiting for a reply.
Recorded approvals and handoff instructions inform the recommendation; they do not
remove this pause.

Once the user chooses the next action in a follow-up, use the appropriate skill,
such as [chunk-start](../chunk-start/SKILL.md) for implementation, investigation,
or unfinished chunk work. Reuse valid approval for an unchanged plan; the user
need not repeat plan approval or invoke another skill by name. Honor that action's
completion boundary.

For shared conventions, see
[the overview](../campaign-start/references/campaign-workflow-overview.md).
