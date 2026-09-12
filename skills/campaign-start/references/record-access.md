# Reading and adapting campaign records

## Current context first

Treat orientation as answering a few current questions, not collecting a document set.
Read `STATE.md` first; a compact snapshot can be read in full. If it has grown into a
history, locate its current status, authorization, blockers, and handoff sections.
Then read the campaign purpose, applicable constraints and completion criteria in
`SPEC.md`, and the selected chunk and its dependencies in `PLAN.md`. Use headings to
locate these sections; a file being under 200 lines does not make every section relevant.

Stop orienting once you can explain the purpose, current chunk/status, applicable
approval and restrictions, blockers, and next action. Each additional read should
answer a named gap or a question raised by the actual work. An unclear handoff calls
for targeted investigation or reporting the gap, not loading the whole campaign.
Read `RESULT.md` for outcome/closure questions and decisions when their choice applies.
Do not load every core document, recent report, linked note, or skill for orientation.

State links are pointers, not a reading checklist. For a needed note, read its summary
and scope first, then the specific finding or evidence section that answers the
question. Follow corrections and supersession links when relevant; recency alone does
not establish applicability. Stop following links once the question is answered.

## Locating sections

Search within the selected campaign and relevant paths before widening to other
campaigns. Prefer filenames, headings, and identifiers before matching body text.
For example, replacing the path and chunk/topic with the actual task:

```sh
campaign_dir=docs/campaigns/example
rg -n '^#{1,3} ' "$campaign_dir/SPEC.md" "$campaign_dir/PLAN.md"
rg --files "$campaign_dir/notes" -g '*chunk-2*'
rg -l -F 'parameter ceiling' "$campaign_dir/notes"
rg -n '^#{1,3} ' "$campaign_dir/notes/selected-note.md"
sed -n '35,75p' "$campaign_dir/notes/selected-note.md"
```

Choose line ranges from the headings or matches just found; the numbers above are
illustrative. Use filename-only matches to find candidate notes, then bounded snippets
or section ranges from selected files. Avoid wildcard full-file reads or recursive
content dumps. A per-file match limit does not bound output across a directory; narrow
the files and terms if results are large or truncated. Equivalent search/read tools
are fine. Broaden when evidence is incomplete; no matches do not prove an event absent.

## Who reads the detail

The main session reads current intent, approvals, constraints, and the selected chunk
itself. Keep small direct lookups local; delegate broad source searches before loading
their detail. For implementation, investigation, verification, and documentation
assignments, see [work allocation](work-allocation.md). Execution can require further
source reading after orientation is complete.

## Bounded retrieval with subagents

When a question requires searching multiple records or reconciling earlier findings,
use a read-only subagent if available. Give it the question, campaign path, useful
identifiers, and relevant intent/constraints. Start with minimal context where the
harness supports it; let it inspect sources instead of preloading them in the parent
or forwarding the whole conversation. Choose distinct scopes if several agents help.

Example: "Why did we stop testing parameter values above 0.8? Find the supporting
evidence and any later finding that changed that conclusion. Work read-only. Return
a concise answer with source references and unresolved uncertainty."

The subagent searches selectively too. Ask for a brief answer (normally at most about
500 words) with file/section or line references, relevant contradictions or superseding
evidence, and search limitations. Preserve consequential uncertainty even if it needs
more space; omit full source extracts, logs, and a narration of the search.
It does not modify campaign records. The parent uses the answer, following up on
specific uncertainty or checking a consequential source passage without repeating
the full search. Retrieval supports review; it does not replace the independent
source inspection required to establish review findings.

Small direct lookups need no delegation. If delegation is unavailable, use the same
selective process locally; historical lookup is not blocked on subagent support.
Context isolation can protect the main session while increasing total work or latency.
Do not create a note for every lookup. Retain a brief source pointer in `STATE.md` if
needed for ongoing work; write a new synthesis only when it adds substantive knowledge.

## Searching note summaries

New notes use the same `## Summary` heading and a short block with `When`, `Chunk/run`,
and `Touches`, followed by a 1–2 sentence finding and any unresolved issue. This makes
summaries searchable without a separate index to maintain. After narrowing candidate
filenames or topics, extract only those summary blocks; for example:

```sh
rg -l '^\*\*Touches:\*\*.*normalization' "$campaign_dir/notes" -g '*.md'
rg -n -A 6 '^## Summary$' "$campaign_dir/notes/selected-note.md"
```

For a small candidate set the second command can take several filenames. Do not dump
all summaries from a large folder for routine orientation. `-A 6` is a preview, not a
complete finding: read further if the block is longer or the answer needs evidence.
Search headings or relevant passages in older notes without summaries. No summary or
matching term does not prove absence; broaden when needed. Add summaries only during
authorized documentation updates, preserving original content and timestamps.

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
