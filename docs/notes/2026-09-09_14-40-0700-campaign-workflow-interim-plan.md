# Campaign workflow revision: interim plan

**Created:** 2026-09-09 14:40 -07:00
**Updated:** 2026-09-09 17:11 -07:00
**Status:** Implemented and validated for v2 following the user's execution and release
authorization. This note preserves the implementation plan. See the
[validation report](2026-09-09_17-11-0700-campaign-v2-validation.md) for observed behavior, checks, and limitations.

## Problems and basis

The user reports two behaviors in a repository unavailable to this session:
insignificant entries accumulate in `DECISIONS.md`, and `PLAN.md` becomes a running
execution log. The diagnosis below concerns the shared workflow instructions, not
inspection of that other repository. `acw-testing` is not the source of the report.

The current decision template has a broad relevance rule without explicit exclusions
for routine approvals and execution events. The plan template and procedures assign
status, approvals, handoffs, timestamps, and evidence to `PLAN.md`, requiring updates
even when planned work is unchanged. Preservation guidance can also encourage
accumulation without distinguishing historical records from current-state snapshots.

Source references:

- [Workflow overview](../../skills/campaign-start/references/campaign-workflow-overview.md)
- [Decision template](../../skills/campaign-start/assets/DECISIONS.md)
- [Plan template](../../skills/campaign-start/assets/PLAN.md)
- [Chunk completion](../../skills/chunk-complete/SKILL.md)
- [Campaign cleanup](../../skills/campaign-cleanup/SKILL.md)

## Proposed campaign structure

```text
docs/campaigns/<campaign-name>/
├── SPEC.md          Purpose, scope, and completion criteria
├── PLAN.md          Intended chunks, approach, and assessment methods
├── STATE.md         Current status, authorization, and next action
├── DECISIONS.md     Significant design and experimental choices with rationale
├── RESULT.md        Synthesized outcome, evidence, limitations, and closure
└── notes/           Detailed runs, investigations, reviews, and supporting evidence
```

| Record | Contents | Update rule |
| --- | --- | --- |
| `SPEC.md` | Purpose, research question or intended behavior, scope, completion criteria, constraints, and consequential assumptions. | Change when objectives or requirements change. Move operational campaign status to `STATE.md`. |
| `PLAN.md` | Intended chunks, outcomes, work, dependencies, and assessment methods; later work can remain rough. | Revise the relevant sections when planned work changes. Do not append progress narratives or update merely because execution advances. |
| `STATE.md` | Campaign and chunk statuses, applicable approvals, active restrictions/resource limits, blockers, working branch/worktree, essential evidence links, and next action with a concrete first step. | Maintain one current snapshot by replacing stale values, without accumulating session entries. |
| `DECISIONS.md` | Significant design or experimental choices, reasons, useful alternatives, evidence links, and conditions for reconsideration. | Add entries only when a qualifying decision occurs. Preserve earlier substantive decisions and link superseding decisions. |
| `RESULT.md` | Synthesized outcome against completion criteria, supporting evidence, limitations, follow-ups, and closure approval. | Draft or revise the outcome when useful and record closure when approved; do not use as a run diary. |
| `notes/` | Run provenance and observations, investigations, reviews, and other supporting evidence worth retaining. | Use one note per coherent activity, with related observations together. Do not create a note for every action, lookup, or session. |

Keep completed chunks' intended work and assessment criteria in `PLAN.md`; completion
status and evidence pointers belong in `STATE.md`. Actual changes to planned work
still revise the plan in place. A significant rationale belongs in `DECISIONS.md`.

Plan/spec approval belongs in `STATE.md`, identifying the approved scope/revision and
timestamp. Preserve applicable approval and active restrictions across updates;
routine state edits do not invalidate approval of an unchanged plan. Closure approval
belongs in `RESULT.md`; the current campaign status in `STATE.md` reflects it.

## Admission rule for decisions

Record significant engineering design or experimental decisions that establish or
materially change scope, methods, defaults, planned tests, or acceptance criteria.
Explain the choice and its rationale. Routine approvals, execution events, status
changes, and completion announcements do not warrant entries by themselves. Leave
`DECISIONS.md` unchanged when no qualifying decision occurred.

When authorization includes a substantive change, record the change and rationale,
not a separate entry merely saying that the user approved it.

| Event | Record placement |
| --- | --- |
| User approves an already planned simulation | `STATE.md` if authorization must survive the session; no decision entry. |
| Simulation starts or finishes | Status in `STATE.md`; configuration, observations, and outputs in its run note. |
| Surprising result | Run/investigation note; current uncertainty in `STATE.md` when it affects the next action. |
| Default parameters change | Rationale in `DECISIONS.md`; revise `PLAN.md` if planned work changes. |
| Planned test is cancelled | Revise `PLAN.md`; record the cancellation and rationale in `DECISIONS.md`; revise `SPEC.md` if completion criteria change. |
| Review identifies additional necessary work | Findings in the review note; revise `PLAN.md` if planned work changes; current blockers in `STATE.md`. |
| Campaign closes | Outcome and closure approval in `RESULT.md`; closed status and any next action in `STATE.md`. |

## Notes and selective retrieval

Keep `notes/` flat initially. Use the existing timestamp filename convention,
descriptive topics, and consistent chunk/run identifiers. Start substantive notes
with a short summary of their question, finding, and unresolved issues. Link later
corrections or superseding findings so recency alone does not determine relevance.
Do not require a separate notes index initially.

Essential campaign knowledge should be available without reconstructing history:
choices in `DECISIONS.md`, planned obligations in `PLAN.md`, current obligations and
navigation in `STATE.md`, and synthesized outcomes in `RESULT.md`.

The main agent should:

1. Read `STATE.md`, relevant spec/plan sections, and directly applicable decisions.
2. Follow a specific source link directly when the needed material is small and known.
3. Delegate a bounded historical question when it requires searching multiple notes
   or reconciling earlier findings. Do not preload the source material in the parent.
4. Use the returned answer and resolve specific uncertainties through targeted
   follow-up or source checks, without repeating the entire search.

A retrieval subagent receives minimal context: the question, campaign path, relevant
constraints, and any useful identifiers. It works read-only, searches filenames,
headings, and matching passages, then inspects relevant context and follows evidence
and supersession links. It returns a concise answer with file/section or line
references, contradictions, superseding evidence, and gaps in search coverage.
An unsuccessful search should not be presented as proof that an event never happened.

Example question: "Why did we stop testing parameter values above 0.8? Identify the
supporting evidence and any later findings that changed that conclusion. Return a
concise answer with source references and unresolved uncertainty. Work read-only."

Do not send every subagent the full campaign history or ask each to read all notes.
This protects the main agent's context but can increase total tokens and latency;
small direct lookups need no delegation. If subagents are unavailable, use the same
selective retrieval procedure locally. Retrieval is not a substitute for substantive
source inspection required by a review.

Do not create a new note for every lookup. If the answer affects ongoing work, retain
a brief pointer to the existing evidence in `STATE.md`. A new durable synthesis is
appropriate only when it adds substantive information.

## Proposed implementation sequence

Implement this as one coordinated workflow revision so the templates and procedures
agree. Use the steps below as reviewable implementation stages.

### 1. Define record ownership and update rules

Update the shared overview and campaign templates together. Add `STATE.md`; move
campaign status out of `SPEC.md`, and move approvals, chunk status, execution
timestamps, handoffs, and current evidence pointers out of `PLAN.md`. Define when
each record should remain unchanged. Tighten decision admission using the examples
above. Keep the templates brief and the current-state snapshot replaceable in place.

### 2. Align all readers and writers

Update campaign start/resume, chunk start/completion, chunk/campaign review, campaign
completion, cleanup, and refresh where relevant. Route review evidence to notes and
current pointers to state; change the plan only when intended work changes. Preserve
existing approval semantics, substantive review requirements, and session boundaries.
Update the README and repository documentation guide to describe the same roles.
Keep substantive shared rules in one place, with short operational reminders where
skills need them independently.

### 3. Add selective retrieval to the existing workflow

Write a shared retrieval procedure and reference it from the relevant skills.
Specify the initial reading set, direct lookup for known small sources, and minimal-
context read-only subagents for bounded questions spanning history. Require compact
answers with references, contradictions, supersession, and search limitations. Avoid
loading the searched corpus in the parent before or after delegation. Support the
same selective process locally when delegation is unavailable.

Start with the existing skills and shared references. A separate retrieval skill,
mandatory notes index, or new automation is not needed for this revision. Any new
abstraction should be justified by a concrete need found during implementation.

### 4. Focus routine cleanup on affected records

This is an additional proposed optimization. Retain the existing cleanup step, but
scope routine chunk cleanup to the current state, affected records and sections,
changed links, and evidence needed to check their consistency. Use the chunk's change
scope and evidence pointers as the starting point. Expand inspection when missing
context, contradictions, or broken references justify it; avoid rereading the entire
notes directory after each chunk.

At campaign closure, reconcile the campaign outcome, completion criteria, dispositions,
and supporting evidence across the campaign. Broader coverage should still use
selective retrieval rather than indiscriminately loading every historical note.
A clean pass need not produce a new note or rewrite unchanged documents.

### 5. Support existing campaigns without losing history

Add adaptation guidance to the migration documentation and affected procedures.
When `STATE.md` is absent, locate existing status, approvals, and handoffs in the
established records. Read-only orientation must still work without creating files.
During an authorized documentation update, introduce state incrementally and move
accumulated history into linked notes while preserving content, timestamps, valid
approvals, substantive decisions, and useful existing paths. Remove ambiguity about
which location holds current state after adaptation. Do not automatically migrate
unrelated campaigns or modify the inaccessible repository that motivated this work.

### 6. Validate routing and retrieval behavior

Check all record references for conflicting old instructions, verify relative links,
and run the existing installer tests to check that the shared assets still distribute
correctly. Structural tests alone do not validate agent behavior.

Use a small representative campaign fixture or walkthrough to check these scenarios:

| Scenario | Expected behavior |
| --- | --- |
| Approve and execute an unchanged planned run | Preserve authorization and update state/run evidence without modifying `PLAN.md` or adding a decision entry. |
| Complete and hand off a chunk | Update status and current pointers; retain the intended plan and replace the current handoff without appending a narrative. |
| Cancel a planned test or change a consequential default | Update the intended work where affected, record the substantive rationale, and update criteria only when those criteria change. |
| Retrieve a historical finding that was later superseded | Return the applicable conclusion with sources and uncertainty; avoid a full-history read by the main agent. |
| Adapt an older campaign | Preserve approval, evidence, and historical content; leave a clear current-state location and working references. |
| Perform routine cleanup with no substantive discrepancy | Inspect the relevant scope and finish without generating a redundant report or rewriting unchanged records. |

Where a representative agent run is practical, inspect its read/write trace for
unnecessary document edits, duplicated evidence loading, and retrieval accuracy.
Measure context or token usage only when the harness exposes it; do not infer token
savings from file count or instruction length. Record any behavioral coverage that
was not exercised rather than presenting a textual walkthrough as an execution test.

## Completion criteria for this update

- The five record roles are consistent across templates, overview, and all skills.
- Routine execution can leave both the plan and decision log unchanged.
- State is a compact current snapshot, with approvals and restrictions retained.
- Agents have a concrete selective-reading and delegated-retrieval procedure.
- Routine cleanup has bounded initial scope and justified expansion.
- Existing campaign records can be used and adapted without losing history.
- Validation distinguishes packaging/link checks from observed agent behavior.

## Next action

Use the v2 guidance for subsequent campaigns and adapt existing records only during
an authorized documentation update. Revisit future workflow changes in a new focused
plan, using the validation findings as context.
