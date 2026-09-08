# Campaign workflow overview

A campaign carries a coherent engineering or research effort across sessions.
Its documents help humans and agents remember what matters. Adapt the workflow
to the work and the user's preferences; a missing heading or skipped ceremony
does not make useful work invalid.

## Project documentation and smaller tasks

Use project documentation to explain the current project and campaign records to
preserve each effort's intent, reasoning, and evidence. See the
[repository documentation guide](repository-documentation.md) when introducing
README, AGENTS.md, development or design guidance, or deciding where a finding belongs.
Adapt existing docs and add files only when useful; this is not a setup checklist.

Work outside a campaign can leave an optional note in
`docs/notes/YYYY-MM-DD-topic.md`. A small fix may need only a commit and relevant
checks. Both small tasks and campaign chunks update affected project guides when
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
| `SPEC.md` | Purpose, scope, desired behavior or research question, success evidence, and consequential unknowns. |
| `PLAN.md` | The current route through session-sized chunks, status, evidence links, and the next action. |
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

## Starting and planning

Interview conversationally. Ask whether this effort is engineering, an experiment,
or a mixture, and listen for the outcome the user actually wants. Explore the
repository and useful previous campaigns to inform follow-up questions. Ask only
questions that matter to the next decision; no coverage questionnaire is required.

For engineering, success may mean a behavior, interface, or verified capability.
For experiments, discuss the question, comparisons, inputs, interpretation, and
resources as relevant. Mixed campaigns may build infrastructure and then use it
to answer a question. A negative or inconclusive result can complete a well-run
investigation.

A chunk aims at something coherent that fits one working session. Describe its
outcome, the work currently expected, and how to assess it. Detail the next chunk;
later chunks can stay rough. A chunk can include setup, several runs, analysis,
or writing. It need not correspond to one commit or one experiment.

Update the plan as new evidence changes the approach. Split unfinished work at a
session boundary, add or reorder chunks, and drop obsolete work with a short reason.
Record consequential changes of scope or interpretation in `DECISIONS.md`.
A changed plan is useful information, not a process failure.

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

A useful note name is `YYYY-MM-DD-<topic>.md`. Review names can include the chunk
and a round suffix. Preserve previous reviews and run evidence rather than
overwriting them; append follow-up verification or write a new linked note.

## Reviews

Review against both the user's intent and the actual implementation or evidence.
For a chunk, inspect the relevant changes and focused checks. For a campaign,
examine the accumulated outcome, integration, assumptions, and unresolved findings.
Do not infer campaign correctness solely from individual chunks being marked done.

Delegate distinct questions to independent subagents when available. Give each the
campaign path, relevant spec/plan, change or artifact scope, and a clear assignment.
Reviewers are read-only: ask for evidence-backed findings, uncertainties, and suggested
dispositions. Do not have reviewers overwrite a shared report or fix code in parallel.
The parent reconciles their findings and owns the report. If delegation is unavailable
or fails, complete the review locally and disclose the reduced independence.

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

Use the harness's available tools for questions, files, Git, and delegation.
If a named helper is not registered, read its linked `SKILL.md` and follow it.
If supporting material is unavailable, preserve the same document roles using
plain Markdown and explain the limitation. No particular tool name, slash-command
syntax, custom agent type, hook, or permission file is part of the workflow contract.
