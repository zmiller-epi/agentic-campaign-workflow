# Campaign workflow overview

A campaign carries a coherent engineering or research effort across sessions.
Its documents help humans and agents remember what matters. Adapt the workflow
to the work and the user's preferences; a missing heading or skipped ceremony
does not make useful work invalid.

## Project documentation and smaller tasks

`repo-init` introduces or refreshes repository-level documentation, usually once
near the start of a project. It can be revisited explicitly as the project changes.
`campaign-start` opens each campaign using the existing project context; it does not
repeat repo setup or require an initialization marker. Completion skills continue
to maintain the project guides affected by their work.

Use project documentation to explain the current project and campaign records to
preserve each effort's intent, reasoning, and evidence. See the
[repository documentation guide](../../repo-init/references/repository-documentation.md) when introducing
README, AGENTS.md, development or design guidance, or deciding where a finding belongs.
Adapt existing docs and add files only when useful; this is not a setup checklist.

Work outside a campaign can leave an optional note in
`docs/notes/YYYY-MM-DD_HH-mm±HHMM-topic.md`. A small fix may need only a commit
and relevant checks. Both small tasks and campaign chunks update affected project guides when
they change how the project is used or understood, linking back to supporting notes
or campaign records. Keep tentative conclusions clearly labeled.

## Shared record

New campaigns normally live in `docs/campaigns/<name>/`. Reuse established project
paths, including the older engineering/experiment campaign folders. When several
campaigns are plausible, identify the intended one before changing its records.
Inspect relevant previous campaigns for context without treating old plans as
instructions for the current campaign. Documents on other branches may not be
visible in the current checkout; use read-only Git inspection when helpful.

| Record | Keep here |
| --- | --- |
| `SPEC.md` | Purpose, scope, desired behavior or research question, completion criteria and evidence, assumptions, and consequential unknowns. |
| `PLAN.md` | The current route through session-sized chunks, plan approval, status, evidence links, and the next action. |
| `DECISIONS.md` | Choices that matter later, why they were made, and what might reopen them. |
| `RESULT.md` | What came out of the campaign, supporting evidence, limitations, follow-ups, and closure approval. |
| `notes/` | Reviews, exploratory thoughts, run records, handoffs, and material that does not belong above. |

Templates in [../assets](../assets) are starting points. Create all four documents
at campaign start, leaving decisions and results brief when there is little to
say. Create `notes/` then, and add entries when they help. An empty notes directory
need not be kept in Git. Avoid duplicate summaries across documents.

Keep the campaign's current status near the top of `SPEC.md`. Plain words such as
draft, active, paused, completed, and abandoned work well; preserve local wording.
`PLAN.md` records chunk state. `RESULT.md` distinguishes a draft from the outcome
the user approved. These are readable conventions, not parser requirements.

## Timestamps

Use `YYYY-MM-DD HH:mm ±HH:MM` for new date stamps in all workflow records,
including creation and update fields, decisions, approvals, status changes,
handoffs, reviews, cleanup notes, and run records. Use a 24-hour clock with
zero-padded hours and minutes and an explicit UTC offset, for example
`2026-09-08 18:35 -07:00`. Seconds are unnecessary for workflow stamps; retain
any finer precision in source logs or experimental evidence.

Use the user or project's established time zone; otherwise use the runtime's
local zone and its actual offset. Read the clock when recording a current event
rather than estimating the time from the conversation. Use the offset applicable
at that instant, including daylight-saving changes; `+00:00` denotes UTC.
For an earlier event, use its evidenced time. If only the recording time is known,
label it `Recorded at` rather than implying it was the event or approval time.
Never fill pending approval, start, or completion times before those events occur.

In filenames, use `YYYY-MM-DD_HH-mm±HHMM-<topic>.md`, for example
`2026-09-08_18-35-0700-chunk-1-review.md`. Replace `±` with the actual `+` or `-`
sign; the filename retains the offset without spaces or colons. Use the record's
creation time for its filename and keep that filename stable when updating it.
Add a suffix such as `-r2` if the timestamp and topic would otherwise collide.

The campaign templates include `Created` and `Updated` fields. Set both when
creating a document; preserve `Created` and advance `Updated` when changing its
content. Record event times alongside approvals, decisions, state changes, and
handoffs where they occur; a document's update time does not replace them.

Apply this convention to new records and new entries in existing documents.
Preserve historical timestamps and filenames, including date-only entries; do not
rename old notes or invent missing hours, minutes, or offsets. An unknown event
time can remain explicitly unknown. Calendar dates that are not event stamps,
such as a publication date or a day-only deadline, can remain dates.

## Starting and planning

Interview conversationally. Ask whether this effort is engineering, an experiment,
or a mixture, and listen for the outcome the user actually wants. Explore the
repository and useful previous campaigns to inform follow-up questions. Probe
consequential assumptions, distinguish them from confirmed facts, and clarify what
evidence would validate them or change the direction. Ask only questions that matter
to the next decision; no coverage questionnaire is required.

For engineering, success may mean a behavior, interface, or verified capability.
For experiments, discuss the question, comparisons, inputs, interpretation, and
resources as relevant. Mixed campaigns may build infrastructure and then use it
to answer a question. A negative or inconclusive result can complete a well-run
investigation. Agree on concrete campaign completion criteria and the evidence
needed to assess them, including acceptance examples or thresholds where useful.
For research, define sufficient evidence and stopping conditions, including how
negative or inconclusive results could meet the criteria.

Present the spec, plan, completion criteria, assumptions, and unresolved choices for
explicit user approval before beginning implementation, experiments, or other campaign
chunks. Interviewing, read-only context gathering, and drafting campaign records can
continue while approval is pending; keep the campaign draft and the next action in
`PLAN.md` focused on review or revision. A request to start or proceed does not approve
an unseen plan. Once approved, record approval and its timestamp in `PLAN.md`
and mark the campaign active, leaving the first chunk planned. `campaign-start` ends here with a
documented handoff; it does not execute the approved plan. Reuse approval for an
unchanged plan; present material revisions to scope, approach, or completion criteria
for approval before executing them.

A chunk aims at something coherent that fits one working session, including focused
checks, review, and documentation. Describe its outcome, the work currently expected,
and how to assess it. Detail the next chunk; later chunks can stay rough. A chunk can
include setup, several runs, analysis, or writing. It need not correspond to one commit
or one experiment.

Update the plan as new evidence changes the approach. Split unfinished work at a
session boundary, add or reorder chunks, and drop obsolete work with a short reason.
Record consequential changes of scope or interpretation in `DECISIONS.md`.
A changed plan is useful information, not a process failure.

## Session boundaries and handoffs

End the current session's work after approved campaign planning, after chunk
completion and cleanup, and after campaign completion. Finish the records and
checkpoints for that boundary, then stop. Do not automatically start the first or
next chunk, invoke resume, move into campaign review/closure after the final chunk,
or begin a follow-up campaign. Plan approval authorizes the plan; it does not make
`campaign-start` an execution skill.

At each boundary, suggest that the user clear context or start a new session before
continuing. Provide a ready-to-use prompt naming the campaign path and next chunk,
review, closure, or follow-up action. Do not clear context on the user's behalf.
For a closed campaign with no follow-ups, simply suggest a fresh session for new work.

Keep a durable handoff in `PLAN.md`: the handoff timestamp, current state and approvals,
branch or worktree, the next action and its first concrete step, unresolved questions,
and relevant evidence/notes. The next session must be able to proceed from these
records without the previous chat history. A later user request to resume or start the named chunk
can execute that action without reapproving an unchanged plan. Execute one chunk at
a time and honor the next completion boundary.

## Evidence and notes

Choose verification appropriate to the claim. Record what actually ran, the outcome,
and where someone can inspect supporting output. A concise result and a durable link
usually suffice; full terminal transcripts belong in notes only when useful.
State what was not checked. Never invent evidence or approval to fill a template.

For runs that support a research conclusion, record enough provenance to understand
and reproduce them: code revision and relevant uncommitted changes, command or
notebook/configuration, input/data versions, environment and seeds where material,
outputs, failures, and interpretation. Keep large artifacts in an appropriate
artifact location and link them. Missing provenance limits the claim; a commit
hash alone does not capture an uncommitted notebook or changing external data.
Use a clean checkpoint when practical, or retain the relevant patch/configuration.

A useful note name is `YYYY-MM-DD_HH-mm±HHMM-<topic>.md`, following the
[timestamp convention](#timestamps). Review names can include the chunk and a
round suffix. Preserve previous reviews and run evidence rather than overwriting them; append follow-up verification or write a new linked note.

## Reviews

Review against both the user's intent and the actual implementation or evidence.
For a chunk, inspect the relevant changes and focused checks. For a campaign,
examine the accumulated outcome, integration, assumptions, and unresolved findings.
Do not infer campaign correctness solely from individual chunks being marked done.

`chunk-review` and `campaign-review` use independent subagents for substantive
inspection and checks. Keep the calling session to scoping, coordination, and synthesis.
Read only enough summary context to delegate; give reviewers campaign and reference
paths, revision/change or artifact scope, relevant user intent and constraints, and
bounded questions. Use minimal starting context when supported, and let reviewers
read the detailed evidence themselves. Do not preload full diffs, logs, prior reports,
or datasets into the parent context.

Reviewers are read-only: they do not fix code or edit shared reports, and their checks
must not interfere with others' work. Ask for compact, evidence-backed findings,
check outcomes, limitations, and file/line or artifact references, not raw transcripts
or exploratory reasoning. The parent reconciles findings, using targeted follow-ups
or small reference checks rather than repeating the review, and owns the report.
Retry or reassign failed scopes when possible. If delegation is unavailable or
coverage remains incomplete, record the gap and hand off to a dedicated review
session with subagent support; do not perform the detailed review inline or claim
missing reviews passed. Incomplete coverage cannot establish overall readiness.

Reports in `notes/` should explain the scope/revision reviewed, evidence examined
or checks run, findings ordered by consequence, and limitations. For each actionable
finding, explain the impact and next action, with file or artifact references.
Distinguish blocking issues, follow-up work, and suggestions. State when no actionable
findings were found. Link follow-ups from `PLAN.md` so they can be found next session.
An expensive rerun is a choice informed by uncertainty and agreed resource limits,
not a default prerequisite or an arbitrary light/heavy mode.

## Completion and cleanup

`chunk-complete` checks the outcome against the current plan, carries forward useful
notes and decisions, updates chunk status, and checkpoints the work. An unresolved
issue that invalidates the outcome keeps the chunk open. Ordinary completion needs
no new approval when it is already within the user's request.
After its documentation and cleanup checkpoint, it ends with the session handoff
above. Later chunks remain planned, including when the next action is campaign review
or closure rather than implementation.

Run `campaign-cleanup` after chunk completion and while preparing campaign closure.
It can also help after a large plan change or a resume that reveals stale records.
Prefer a subagent with ownership of the selected campaign's documentation. While it
works, the parent avoids editing those same files. Without subagents, do the pass
locally. This is an event-based habit; nothing runs on a clock or in the background
unless the user separately arranges that.

Cleanup reads this overview and looks for misleading status, lost next actions,
unrecorded decisions, orphaned findings, broken links, and duplicated or misplaced
material. It can fix obvious clerical issues and report uncertainty. It does not
invent missing research history, reinterpret conclusions, approve completion, or
turn cosmetic preferences into gates. Put substantial cleanup findings in a note;
a short summary suffices for trivial edits. Check for affected project guidance too;
with campaign-only ownership, report needed repo-level updates to the parent. The
parent updates those guides and keeps the campaign's supporting history linked.

`campaign-complete` prepares `RESULT.md` for a completed or abandoned campaign,
runs cleanup, then shows the concrete outcome and unresolved limitations to the user.
Obtain approval of that result and proposed closure before marking the campaign
closed. A request to run the completion skill starts this process; it does not
approve an outcome the user has not seen. Reuse approval already given for the
unchanged result. If cleanup materially changes the result, show the revision.
Paused work can stay open with a clear next action.
Record the approved disposition and its timestamp, checkpoint the documents, then
stop and suggest a fresh session before follow-ups, paused work, or a new campaign.

## Git collaboration

Prefer frequent, focused commits on a working branch whenever there is a useful
recovery point. Stage only task-owned paths or hunks and inspect the staged diff,
including changes already staged by others. Use informative messages; WIP commits
are fine. Checkpoint code before a significant experiment when practical.

Reuse an appropriate working branch and starting state. For a new branch, follow
project or harness naming preferences. Identify the integration branch instead of
assuming it is named main. Use a separate worktree for concurrent campaigns; do not
switch a checkout out from under another session. Preserve unrelated changes and
avoid destructive cleanup, resets, or branch deletion to satisfy workflow conventions.
The document workflow can still be used without Git.

Keep the human involved in integration into the main branch and meaningful milestone
or release tags: present the content and proposed message for approval, honoring any
specific prior authorization. No per-chunk tags, fixed squash policy, branch deletion,
or history rewrite is required. Closure approval does not authorize merging, pushing,
or publishing. Preserve abandoned work and record why it stopped.

## Harness portability

Skills use shared Markdown instructions and links relative to their own locations.
Resolve those links from the loaded skill file, not the project working directory.
Campaign paths are relative to the user's project. Copy the full skills set together;
shared templates and this overview travel inside `campaign-start`.

During workflow development, projects can link their installed skills to one source
checkout using the installer's `--dev` option. Use [campaign-refresh](../../campaign-refresh/SKILL.md)
when asked to reload those instructions in an ongoing task, or pull source updates
before reloading. Refresh is explicit; it does not run on a timer, restart campaigns,
or retroactively invalidate prior work. Preserve the consuming project's records and
approval boundaries while adopting changed instructions.

Use the harness's available tools for questions, files, Git, and delegation.
If a named helper is not registered, read its linked `SKILL.md` and follow it.
If supporting material is unavailable, preserve the same document roles using
plain Markdown and explain the limitation. No particular tool name, slash-command
syntax, custom agent type, hook, or permission file is part of the workflow contract.
