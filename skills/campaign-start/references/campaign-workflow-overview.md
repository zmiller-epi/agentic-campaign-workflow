# Campaign workflow overview

A campaign carries engineering or research work across sessions. Adapt its records
to the work and the user's preferences.
This overview defines shared conventions; individual skills own their procedures.

## Project documentation and smaller tasks

Use [repo-init](../../repo-init/SKILL.md) to introduce or refresh project docs;
campaigns reuse that context. Project guides describe current behavior, while
campaign records preserve intent, decisions, and evidence. Update affected guides
as work changes the project, following the
[repository documentation guide](../../repo-init/references/repository-documentation.md).
Small tasks can use an optional note in `docs/notes/` without opening a campaign.

## Shared record

New campaigns normally live in `docs/campaigns/<name>/`; preserve established paths
and existing content. Identify the intended campaign before editing, and treat
previous campaigns as context rather than instructions for current work.

| Record | Keep here |
| --- | --- |
| `SPEC.md` | Purpose, scope, completion criteria, assumptions, and consequential unknowns. |
| `PLAN.md` | Intended chunks, outcomes, approach, dependencies, and assessment methods. |
| `STATE.md` | Current campaign/chunk status, approvals, restrictions, evidence pointers, and next action. |
| `DECISIONS.md` | Significant design or experimental choices, reasons, and what might reopen them. |
| `RESULT.md` | Outcome, evidence, limitations, follow-ups, and closure approval. |
| `notes/` | Reviews, run records, exploration, and supporting context. |

Create the five documents and `notes/` at campaign start using the
[templates](../assets), keeping empty records brief. Keep campaign and chunk status
in `STATE.md`, and `RESULT.md` draft until approved. Preserve `Created`; advance
`Updated` only when content changes.

Revise `PLAN.md` in place only when intended work changes; completed chunks retain
their intended work and assessment criteria. Routine execution and completion can
leave both the plan and decision log unchanged. `DECISIONS.md` admits significant
choices about scope, methods, defaults, planned tests, or acceptance criteria, such
as cancelling a planned test or changing default parameters. Routine approvals,
execution events, and review/closure announcements do not qualify by themselves.

Maintain `STATE.md` as one compact snapshot, replacing stale values rather than
appending session entries. Keep applicable approvals, approved scope/revision, active
restrictions, and essential evidence links. Preserve unique useful history in linked
notes before replacing its only copy; avoid duplicating information already recorded.
Closure approval stays in `RESULT.md`.

## Reading records

Start with current state and the relevant spec/plan sections. Load notes to answer
specific questions. Follow [record access](record-access.md) for selective reading,
bounded subagent searches across history, or using an older campaign without
`STATE.md`. Essential current obligations should be reachable from state without
reconstructing the campaign's history.

## Timestamps

Use `YYYY-MM-DD HH:mm ±HH:MM` in records (e.g., `2026-09-08 18:35 -07:00`) and
`YYYY-MM-DD_HH-mm±HHMM-<topic>.md` for new filenames, using the user/project time
zone or the runtime's local zone if unspecified.
Read the clock for current events; preserve historical timestamps and filenames,
and leave unknown event times unknown.

## Starting and planning

[campaign-start](../SKILL.md) owns the interview, spec, plan, and completion criteria.
Obtain the user's approval of the presented plan before execution; reuse approval
for unchanged work and seek approval for material revisions.
Plan in session-sized chunks with concrete outcomes and checks, refining later
work as evidence develops and recording consequential changes in `DECISIONS.md`.

## Session boundaries and handoffs

Stop after approved campaign planning, chunk completion and cleanup, and campaign
completion. Do not automatically begin another chunk, review, closure, or campaign.
Suggest clearing context or starting a new session, with a ready-to-use prompt
naming the campaign and next action; leave clearing context to the user.

Refresh the handoff in `STATE.md`: applicable approvals, branch or worktree,
essential evidence links, unresolved questions, and the next action's first step.
Use the snapshot's `Updated` timestamp; a fresh session must be able to continue
from these records without a history of earlier handoffs.
[campaign-resume](../../campaign-resume/SKILL.md) inspects the current state, orients
the user, and ends the turn waiting for the user to choose the next action. Recorded
approval or a handoff does not bypass this pause. Once the user chooses execution,
reuse valid approval for an unchanged plan; work one chunk at a time and honor the
next completion boundary.

## Evidence and notes

Match verification to the claim. Record what ran, its outcome, supporting evidence,
and what remains unchecked. Never invent evidence or approval.
For research runs, retain enough provenance to reproduce and interpret the result:
code revision and relevant uncommitted changes, commands/configuration, input versions,
material environment/seeds, outputs, and limitations. Link to large artifacts where stored.
Negative or inconclusive results can satisfy an investigation's completion criteria.

Use one note per coherent run, investigation, or review, with related observations
together. Start with a short summary of the question, finding, and unresolved issues.
Name notes using the [timestamp convention](#timestamps), a descriptive topic, and
chunk/run identifiers where useful. Add a round suffix to avoid collisions. Preserve
earlier reports and run evidence, linking corrections and superseding findings.
Routine actions, handoffs, and lookups do not each need a note or an index entry.

## Reviews

Use [chunk-review](../../chunk-review/SKILL.md) and
[campaign-review](../../campaign-review/SKILL.md) for independent review against
user intent and actual work. Reviewers perform substantive inspection read-only;
the parent scopes, coordinates, and synthesizes rather than repeating their review.
If delegation or coverage is unavailable, record the gap and hand off for review
with subagent support; do not substitute detailed parent review or claim readiness.

Reports in `notes/` identify scope/revision, evidence, findings, limitations, and
next actions. Keep the applicable assessment, blockers, and report link in `STATE.md`;
revise `PLAN.md` only if findings change intended work. Follow-up reports link the
findings they resolve. `RESULT.md` synthesizes review evidence at closure. Campaign
review assesses integration and the accumulated outcome.
Choose costly reruns according to uncertainty and authorized resource limits.

## Completion and cleanup

[chunk-complete](../../chunk-complete/SKILL.md) checks review and outcome evidence,
updates records and affected guides, checkpoints the work, and leaves a handoff.
Blocking issues keep the chunk open; routine completion within the user's request
needs no additional approval.

Run [campaign-cleanup](../../campaign-cleanup/SKILL.md) after chunk completion and
while preparing campaign closure, or when records drift. It repairs documentation
within its assigned ownership. Routine cleanup starts with affected records and
links, expanding when discrepancies warrant it. Closure reconciles the outcome and
evidence across the campaign. Preserve history and surface uncertainty; a clean pass
needs no report or rewrite of unchanged records.

[campaign-complete](../../campaign-complete/SKILL.md) prepares `RESULT.md`, runs
cleanup, and obtains approval of the concrete result and disposition before closure.
Reuse approval for an unchanged result; keep paused work open with a resume action.
Record the approved status and timestamp, checkpoint, and honor the session boundary.

## Git collaboration

Make frequent, focused checkpoint commits on an appropriate working branch; WIP
commits are fine. Stage only task-owned paths or hunks and inspect the staged diff,
including anything already staged. Checkpoint before significant experiments when practical.

Reuse suitable branches, follow project/harness naming, and identify the integration
branch rather than assuming `main`. Use separate worktrees for concurrent campaigns;
preserve others' changes and avoid disruptive branch switches or destructive cleanup.
The document workflow also works without Git.

Obtain authorization for integration and meaningful tags, including their content
and messages; honor specific prior authorization. Closure does not authorize merging,
pushing, or publishing. No fixed squash policy, per-chunk tags, branch deletion, or
history rewrite is required; preserve abandoned work and record why it stopped.

## Harness portability

Resolve skill links relative to the loaded skill file and campaign paths relative
to the user's project. Copy the full skill set together so shared references and
templates remain available. If a skill is not registered, read its linked `SKILL.md`;
use the harness's available tools and explain missing capabilities.

Development installs can link to one source checkout with `--dev`.
[campaign-refresh](../../campaign-refresh/SKILL.md) reloads instructions explicitly
and pulls upstream only when requested, preserving campaign records and approvals.
