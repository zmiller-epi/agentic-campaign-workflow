---
name: chunk-review
description: Delegate a campaign chunk review to independent subagents, keeping detailed inspection out of the calling session, and record an evidence-backed report.
---

# Review a chunk

Use concise, plain language in records and responses. Keep needed facts, reasons,
evidence, uncertainty, and next actions; omit filler and repeated context.

Use `YYYY-MM-DD HH:mm ±HH:MM` for every new date stamp this skill records. Follow
[the shared timestamp convention](../campaign-start/references/campaign-workflow-overview.md#timestamps)
for filenames, time zones, and preserving historical records.

Keep the calling session focused on coordination and synthesis. Resolve the campaign
and chunk from current state, and read only enough of `SPEC.md` and `PLAN.md` to
identify its intended outcome and assessment criteria. Use
[record access](../campaign-start/references/record-access.md) for historical lookup or legacy state. Identify the revision/diff boundary, relevant paths,
and any uncommitted changes included. If the boundary cannot be reconstructed, state
the scope used. Leave detailed code, artifact, and log inspection to reviewers.

**Use independent subagents for the substantive review**, assigning bounded questions.
For example, one can assess agreement with the spec while another examines correctness,
regressions, or the validity of experimental evidence. Choose the number and scope
to fit the work rather than requiring a fixed panel.

Start reviewers with minimal context when supported. Give each the campaign path,
chunk identifier, relevant skill/reference paths, revision/diff or artifact scope,
the user's relevant intent and constraints, and a specific question. Reviewers read
the relevant spec, plan, decisions, changes, and supporting artifacts themselves;
do not preload that evidence in the parent or forward the whole conversation.

Give reviewers read-only ownership. They are not alone in the workspace: they must
not edit, revert others' work, fix implementation, overwrite shared reports, or run
checks that interfere with other reviewers. They perform their assigned review
directly rather than recursively invoking this coordinating skill.

Have reviewers inspect the work and run focused checks within the user's authorization
and resource limits. They can reuse relevant recent evidence covering the current work.
For research, assign checks of the question, comparisons, provenance, analysis, and
whether the conclusion follows from the results. Avoid substituting process compliance
for technical review.

Ask for compact results: scope/revision, assessment, findings with supporting file/line
or artifact references, checks and outcomes, and limitations. Keep full diffs, logs,
transcripts, and exploratory reasoning out of their replies. Wait for and reconcile
their findings. Resolve uncertainty through targeted reviewer follow-ups or small
reference checks; do not duplicate the full inspection in the parent. The parent owns
the report and current-state pointers.

Retry or reassign failed reviews where possible; never count unreturned reviews as
passes. If delegation is unavailable or coverage remains incomplete, record the gap
and provide a handoff for a dedicated review session. Do not fall back to a detailed
review in the calling session or claim independent checks that did not happen.
The handoff should identify the missing scope and need for subagent support.

Write a readable report under `notes/`, such as
`YYYY-MM-DD_HH-mm±HHMM-chunk-<name>-review.md`; include the review timestamp
in the report. Use a new suffix or a linked follow-up for later rounds. Adapt the
[note template](../campaign-start/assets/NOTE.md), with a short summary and searchable
scope/finding headings. Aim for about 200 lines or fewer, linking substantial detail
without omitting actionable findings or coverage gaps. Include:

- The scope and revision reviewed, checks/evidence, and reviewer coverage.
- Findings ordered by impact, each with supporting references and a proposed next action.
- A clear assessment of readiness and what remains unverified.

Confirm findings before presenting them; label uncertain concerns accordingly.
Link the report from `STATE.md` with a brief current assessment, blockers, and next
action. Revise `PLAN.md` only when findings change intended work; routine review needs
no decision entry. Keep old findings traceable when later reports resolve them, and
refresh state to point to the applicable assessment without accumulating review history. Report when no actionable
issues were found within the reviewed scope; incomplete coverage cannot establish
overall readiness. Give the user a concise assessment and consequential findings with
a link to the report. Review itself does not mark the chunk complete.

For shared report and evidence conventions, see
[the overview](../campaign-start/references/campaign-workflow-overview.md).
