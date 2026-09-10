# Reading and adapting campaign records

## Current context first

Read `STATE.md`, the relevant `SPEC.md` and `PLAN.md` sections, and directly applicable
decisions. Follow state links for the evidence or unresolved question needed by the
current action. Read `RESULT.md` when assessing the outcome or closure. Do not load
every note, every decision, or all recent reports as routine orientation.

For a known small source, open the relevant section directly. For historical questions,
search filenames, identifiers, headings, or matching passages first, then inspect the
surrounding context. Prefer filename-only matches or bounded snippets; narrow broad
queries before returning large result sets. Use available text search (such as `rg`)
and follow references,
corrections, and supersession links; recency alone does not establish applicability.
Broaden terms or scope when the evidence is incomplete. Search failures do not prove
that an event never happened.

## Bounded retrieval with subagents

When a question requires searching multiple records or reconciling earlier findings,
use a read-only subagent if available. Give it the question, campaign path, useful
identifiers, and relevant intent/constraints. Start with minimal context where the
harness supports it; let it inspect sources instead of preloading them in the parent
or forwarding the whole conversation. Choose distinct scopes if several agents help.

Example: "Why did we stop testing parameter values above 0.8? Find the supporting
evidence and any later finding that changed that conclusion. Work read-only. Return
a concise answer with source references and unresolved uncertainty."

The subagent searches selectively too. It returns the answer, file/section or line
references, relevant contradictions or superseding evidence, and search limitations.
It does not modify campaign records. The parent uses the answer, following up on
specific uncertainty or checking a consequential source passage without repeating
the full search. Retrieval supports review; it does not replace the independent
source inspection required to establish review findings.

Small direct lookups need no delegation. If delegation is unavailable, use the same
selective process locally; historical lookup is not blocked on subagent support.
Context isolation can protect the main session while increasing total work or latency.
Do not create a note for every lookup. Retain a brief source pointer in `STATE.md` if
needed for ongoing work; write a new synthesis only when it adds substantive knowledge.

## Existing campaigns

If `STATE.md` is absent, inspect the established status/approval/handoff sections in
`SPEC.md`, `PLAN.md`, or other existing records and follow their relevant links.
Read-only orientation stays read-only: report ambiguity or drift rather than creating
files. Missing state is not grounds to restart work or require repeat approval.

During an authorized documentation update, introduce [STATE.md](../assets/STATE.md)
when useful, preserving applicable approvals, their timestamps and scope, active
restrictions, chunk status, and the current next action. Identify it as the current
state location. Replace old operational sections with a pointer so there are no
competing current snapshots; preserve historical content before removing its only copy.

When separating accumulated history from a plan or decision log, first inspect it.
Relocate useful historical passages into linked notes, preserving their wording,
timestamps, and evidence; repair relative links and leave a traceable pointer at the
old location. Keep substantive decisions and intended work in their proper records.
Existing `NOTES.md`, `REVIEW.md`, `RESULTS.md`, and `experiments/` can remain as sources;
do not rename whole campaigns or rewrite history merely to match templates. Surface
conflicting approvals or conclusions rather than choosing silently. Updating workflow
instructions does not itself authorize migration of campaign records.
