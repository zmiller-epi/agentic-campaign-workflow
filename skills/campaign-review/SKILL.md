---
name: campaign-review
description: Review an engineering or research campaign in depth against its intent, implementation, and evidence, then write a report in its notes.
---

# Review a campaign

Resolve the campaign and read its `SPEC.md`, living `PLAN.md`, important decisions,
draft or existing `RESULT.md`, and relevant notes. Review the actual accumulated
changes and artifacts as well as individual chunk reports.

Choose questions that could change the assessment: does the delivered behavior meet
the purpose, do components work together, do experiments support the claimed result,
and are important assumptions or failure modes still untested? For mixed campaigns,
cover both the infrastructure and the conclusions drawn with it.

Use independent subagents when available for bounded, complementary questions.
Give each the campaign path, relevant revision/diff or artifacts, and a read-only
assignment. Reviewers are not alone in the workspace and must not edit or revert
others' work. Coordinate checks with side effects so they do not interfere.
Wait for their results and reconcile evidence; disclose missing or failed reviews
and finish locally if delegation is unavailable.

Run meaningful integration or reproduction checks where they reduce real uncertainty.
Choose reruns based on the evidence and the user's resource limits. If a costly run
would exceed existing authorization, propose it and continue the artifact review.
State what inspection and existing evidence cannot establish. Do not treat old passing
chunk reviews as proof that the whole campaign is correct.

Write a new report in `notes/`, for example `YYYY-MM-DD-campaign-review.md`, with
a suffix for later rounds. Explain the scope/revisions reviewed, evidence and checks,
findings ordered by consequence, limitations, and whether the intended outcome is
supported. Give actionable findings clear next steps and supporting file/artifact links.
Preserve earlier reports and link later resolutions.

Link the report and any remediation chunks or follow-ups from `PLAN.md`.
Summarize what is ready, what needs work, and what remains uncertain for the user.
This skill writes a review; it does not close, merge, or publish the campaign.
For conventions, see
[the overview](../campaign-start/references/campaign-workflow-overview.md).
