# Repository documentation

Keep a small, maintained description of the current project alongside its work
history. A new human or agent should be able to understand and use the project
without reconstructing it from old campaigns.

Read this guide when setting up project documentation, deciding where a finding
belongs, or updating documentation after work. These are suggested locations and
roles; follow useful existing project conventions and create files only when they
have content worth maintaining.

## A starting structure

```text
README.md
AGENTS.md
CLAUDE.md -> AGENTS.md
docs/
  development.md
  design.md
  notes/
  campaigns/
```

Start with a README, a small AGENTS.md, and development guidance where useful.
Add design.md when there is something important to explain beyond the code and
commands. Empty directories or placeholder documents are unnecessary.

| Record | Purpose |
| --- | --- |
| `README.md` | The entry point: purpose, intended users, inputs and outputs, a small working example, and links to further documentation. |
| `AGENTS.md` | Brief project-specific working guidance: important constraints, non-obvious pitfalls, and pointers explaining when to read other documents. |
| `CLAUDE.md` | A relative symlink to AGENTS.md when instructions are shared; an `@AGENTS.md` import can accommodate Claude-specific additions. |
| `docs/development.md` | Practical setup, common commands, checks, and recurring troubleshooting. Include prerequisites and expected outcomes; distinguish smoke tests from expensive full runs. |
| `docs/design.md` | How the project currently works: components, interfaces, data flow, methods, assumptions, and the reasons for consequential choices. |
| `docs/notes/` | Standalone investigations, debugging findings, small experiments, reviews, and unfinished thoughts worth preserving. |
| `docs/campaigns/` | Larger efforts with their own spec, living plan, decisions, results, and working notes. |

For a research project, design.md can explain the analysis pipeline and how to
interpret its outputs. Split out `docs/data.md` or `docs/methods.md` when acquisition,
data versions and access, processing, or methodology need substantial treatment.
Link to configuration definitions and environment files instead of duplicating
their contents. Keep large outputs in their artifact location and link to them.

The README can serve as the documentation index until another index would help.
Use descriptive headings, concrete commands with their working directory and
expected outcome, and links to the relevant code, configuration, or evidence.
Distinguish verified behavior, assumptions, and planned work. Keep routine project
knowledge in the appropriate guide so AGENTS.md remains small. A brief AGENTS.md
pointer can name the project's notes and campaign locations and link the installed
workflow guide; keep the detailed conventions here instead of copying them there.

## Introducing this into an existing project

Read the current documentation, inspect the relevant implementation, and use the
user's context before writing. Preserve project-specific facts and adapt existing
guides rather than reorganizing them just to match this layout.

Within an authorized setup task, create or improve the smallest useful entry point
and development guidance from what is known. Record consequential unknowns honestly;
do not invent commands, methods, or project constraints to fill headings. When more
investigation is needed, include that work in the current plan or note.

If AGENTS.md and CLAUDE.md both exist, reconcile their distinct content before
replacing either. Use a relative `CLAUDE.md -> AGENTS.md` link only when their content
is shared. Keep Claude-specific additions in a regular CLAUDE.md with an import.
The skill installer installs skills; it does not overwrite project documentation
or set up these instruction files.

## Work without a campaign

Small work can be requested and completed directly. A self-explanatory fix may need
only a focused commit, appropriate checks, and an update to any affected guide.

When an investigation leaves useful context, write one optional note such as
`docs/notes/YYYY-MM-DD-topic.md`. Include the reason for the work, what happened,
supporting evidence, and any next action as useful. These are prompts, not required
fields. Record a meaningful decision and its reason in that same note; a standalone
task needs no separate spec, plan, decision log, or completion ceremony.

For a small experiment, retain enough code, input/configuration, command, environment,
and output provenance to understand its result. Separate observations from interpretation.
A review can be appended or linked in the same note. If the work grows into a campaign,
link the original note from the new campaign and preserve its history.

## Keeping project docs and campaigns connected

When work changes how someone should understand or use the project, update the
relevant project documentation as part of the work. This applies to small tasks and
campaign chunks. The current documentation should describe the code and supported
methods on the branch being reviewed.

Keep the reasoning and evidence in their original campaign or note. Summarize what
a current user needs in the maintained guide, with a link back when the reasoning
matters. For example, a normalization change can have its alternatives in DECISIONS.md,
comparative evidence in RESULT.md, current methodology in design.md, and revised
commands in development.md. Each record has a different job.

Do not present proposed changes, abandoned approaches, or a draft research conclusion
as established project behavior. Label uncertainty and link to the evidence.
Completion should reconcile affected guides with what was actually delivered or learned.
Cleanup can flag stale project guidance, but a subagent assigned only campaign documents
reports those changes to the parent rather than editing outside its ownership.

This approach borrows the distinction between practical guidance, reference, and
explanation from [Diátaxis](https://diataxis.fr/start-here/), which also recommends
[growing documentation incrementally](https://diataxis.fr/how-to-use-diataxis/).
