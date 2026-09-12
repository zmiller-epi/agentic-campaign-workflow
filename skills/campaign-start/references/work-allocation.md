# Allocating campaign work

At chunk start and when substantial new work appears, decide what can be delegated.
Use subagents beyond review when a bounded task can proceed independently alongside
useful main-session work, or a broad investigation would consume the main context.
Choose ownership before loading the detail. Honor user scope, resource limits, and
harness rules; more agents are not a goal.

## Choose the assignment

| Work | Main session | Useful subagent assignment |
| --- | --- | --- |
| Orientation and planning | User conversation, current spec/state, scope and acceptance decisions | Resolve an unknown across prior campaigns or unfamiliar sources. |
| Implementation | Small fixes, tightly coupled edits, shared interfaces, integration | Build a bounded component with clear inputs/outputs and separate file ownership. |
| Investigation | Frame the question and synthesize the conclusion | Inspect one hypothesis, source set, dataset, or method; return evidence and limitations. |
| Verification | Quick checks and final integration checks | Reproduce a failure or check a distinct behavior in an isolated scope. |
| Documentation | Decisions and the main handoff | Consolidate affected records or update a specific guide after behavior is settled. |
| Review | Scope, coordination, synthesis | Independent source inspection under the chunk/campaign review skills. |

A direct lookup, short edit, or task needed immediately to choose the next step
usually stays local. A substantial historical lookup can justify delegation for
context isolation even if the parent must wait. Avoid agents for every file or step.
Sequence shared-file edits or use separate worktrees where appropriate.

## Give a bounded assignment

Supply the question/deliverable, campaign/chunk, source paths and revision, relevant
intent/constraints, and completion criteria. Specify read-only access or exact files/
worktree to edit, authorized checks, and resource limits. Writers must preserve
others' changes; only one agent owns a shared record or report at a time.

Start with minimal context when supported. Send paths and a compact brief, not the
whole conversation, source dumps, or full diffs. Subagents use
[record access](record-access.md) and perform the assigned task directly without
recursively launching the campaign workflow. Continue useful work without duplicating
their assignment.

Ask for a compact return: outcome, changed files or source/section references, checks
and results, unresolved findings, and limitations. About 500 words is a useful default
for retrieval/investigation; link detail and preserve material uncertainty. An
implementation assignment returns edits and validation, not only suggestions.

## Integrate and handle gaps

Wait for dependent results. Inspect relevant edits or consequential evidence, resolve
conflicts, and run appropriate integration checks without repeating the investigation.
Partial or failed work is a gap, not a pass. Agent activity itself needs no note.

The main session owns decisions, integration, authorization, and the handoff.
Delegation grants no extra scope, spending, or publishing permission. Implementers
cannot serve as independent reviewers of their own work. If delegation is unavailable
or unhelpful, do bounded work locally with selective reads; review skills retain their
explicit independent-review requirement and fallback.
