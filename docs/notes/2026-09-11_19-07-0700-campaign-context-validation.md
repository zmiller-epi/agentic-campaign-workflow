# Campaign context and writing guidance

**Created:** 2026-09-11 19:07 -07:00
**Updated:** 2026-09-11 19:07 -07:00
**Kind:** investigation

## Summary
**When:** 2026-09-11 19:07 -07:00
**Chunk/run:** standalone; codex/reduce-orientation-context
**Touches:** campaign-resume, chunk-start, campaign-cleanup, note summaries, subagents
The v2 workflow requested selective reading but lacked concrete stopping rules,
a shared note format, and general execution delegation guidance. The new defaults
passed synthetic checks; the reported 200k-token sessions remain unmeasured.

## Scope
Compared shared skills at remote main `7fa2495` with this branch's changes. Existing
campaign records were preserved. Independent agents exercised resume and cleanup
in temporary campaigns; this was not a benchmark of real user sessions.

## Findings
- [Record access](../../skills/campaign-start/references/record-access.md) now defines
  targeted searches and an orientation stopping point. State links name sections
  and the questions they answer.
- [Notes](../../skills/campaign-start/assets/NOTE.md) use a searchable summary block
  and a soft 200-line target. Summaries replace a separate notes index.
- [Work allocation](../../skills/campaign-start/references/work-allocation.md) covers
  investigation, implementation, verification, and documentation beyond review.
- Cleanup consolidates current prose and adds summaries while preserving history.
  Every skill carries a concise, plain-language writing default.

## Evidence
- `python3 -m unittest discover -s tests -v`: 28 passed, including installed links
  and shared assets through both harness layouts.
- Skill-creator `quick_validate.py`: all ten skills passed. PyYAML was installed in
  a temporary environment because the default Python lacked that dependency.
- Resume trial: 61 notes totaling 22,696 lines. The evaluator reported about 800
  tokens of campaign text read from state, selected spec/plan sections, and one
  review finding. It inspected the small implementation and paused without edits.
- Cleanup trial: only state and the assigned run note changed. Direct checks
  confirmed all 280 evidence cases, historical times, approval, restriction, open
  chunk status, and five unassigned files were preserved. Summary search examples
  located the relevant note and returned its metadata and finding.
- `git diff --check`: passed.

## Open questions and next actions
The orientation volume is an evaluator estimate, not a tokenizer measurement or
before/after comparison. The checks do not establish a real-session token reduction
or measure general delegation frequency. Verify those in a fresh working session;
use its read trace to identify any remaining unnecessary reads or stale instructions.
