---
name: campaign-review
description: Delegate an engineering or research campaign review to independent subagents, keeping detailed inspection out of the calling session, and record an evidence-backed report.
---

# Review a campaign

Use concise, plain language in records and responses. Keep needed facts, reasons,
evidence, uncertainty, and next actions; omit filler and repeated context.

Use `YYYY-MM-DD HH:mm ±HH:MM` for every new date stamp this skill records. Follow
[the shared timestamp convention](../campaign-start/references/campaign-workflow-overview.md#timestamps)
for filenames, time zones, and preserving historical records.

Keep the calling session focused on coordination and synthesis. Resolve the campaign
and read current state and only enough of `SPEC.md`, `PLAN.md`, and the outcome summary
to scope the review. Use [record access](../campaign-start/references/record-access.md)
for historical lookup or legacy state. Identify the revisions, change boundaries, and artifact locations without
loading full diffs, run logs, prior reports, or large datasets into the parent context.

Choose questions that could change the assessment: does the delivered behavior meet
the purpose, do components work together, do experiments support the claimed result,
and are important assumptions or failure modes still untested? For mixed campaigns,
cover both the infrastructure and the conclusions drawn with it.

**Use independent subagents for the substantive review.** Assign bounded,
complementary questions with enough coverage of the accumulated outcome and integration;
choose the number of reviewers to fit the work. Start reviewers with minimal context
when supported. Give each the campaign path, the relevant skill/reference paths,
revision/diff or artifact scope, the user's relevant intent and constraints, and a
specific review question. Let reviewers read the source evidence themselves instead
of first collecting it in the parent or forwarding the whole conversation.

Reviewers inspect the spec, plan, consequential decisions, results, relevant notes,
actual accumulated changes, and artifacts within their assigned scope. Have them run
meaningful integration or reproduction checks where they reduce uncertainty, within
the user's authorization and resource limits. If a costly run would exceed those
limits, report the proposed check and continue artifact inspection. Old passing chunk
reviews do not prove that the whole campaign is correct.

Give reviewers read-only ownership: they are not alone in the workspace and must
not edit or revert others' work, fix implementation, or overwrite shared reports.
Coordinate checks with side effects so they do not interfere. They perform the assigned
review directly rather than recursively invoking this coordinating skill.

Ask for compact results: scope/revision, assessment, findings ordered by consequence,
supporting file/line or artifact references, checks and outcomes, and limitations.
Keep full diffs, logs, transcripts, and exploratory reasoning out of their replies.
Wait for results and reconcile them into the report. Resolve disputed findings with
a targeted reviewer follow-up or a small reference check; do not repeat the full review
in the parent session. The parent owns the report and current-state pointers.

If a reviewer fails, retry or reassign the missing scope where possible. Never count
an unreturned review as a pass. If delegation is unavailable or coverage remains
incomplete, record the limitation and unreviewed scope, then provide a handoff for
a dedicated review session. Do not fall back to an in-depth review in the calling
session or claim independent verification that did not happen. The handoff should
identify the missing scope and need for subagent support.

Write a new report in `notes/`, for example
`YYYY-MM-DD_HH-mm±HHMM-campaign-review.md`, with a suffix for later rounds.
Include the review timestamp and adapt the [note template](../campaign-start/assets/NOTE.md).
Use a short summary, searchable scope/finding headings, and a target of about 200
lines or fewer; link substantial detail without omitting findings or coverage gaps.
Explain the scope/revisions reviewed, evidence and checks,
findings ordered by consequence, limitations, and whether the intended outcome is
supported by the reviewed scope. Incomplete coverage cannot establish overall readiness.
Give actionable findings clear next steps and supporting file/artifact links.
Preserve earlier reports and link later resolutions.

Link the report from `STATE.md` with the current assessment, unresolved blockers,
and next action. Revise `PLAN.md` only if remediation or follow-ups change intended
work. Significant resulting design/experimental choices belong in `DECISIONS.md`;
routine review does not. Keep detailed findings in the reports they reference.
Give the user a concise assessment, the consequential findings, remaining uncertainty,
and a link to the report; keep detailed evidence in the records it references.
This skill writes a review; it does not close, merge, or publish the campaign.
For conventions, see
[the overview](../campaign-start/references/campaign-workflow-overview.md).
