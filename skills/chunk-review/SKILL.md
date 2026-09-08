---
name: chunk-review
description: Review a campaign chunk with independent subagents when available and write an evidence-backed report in the campaign notes.
---

# Review a chunk

Resolve the campaign and chunk, then read its intended outcome in `SPEC.md` and
`PLAN.md`, relevant decisions, work changes, and supporting artifacts. Identify the
revision or diff and any uncommitted changes included so the review's scope is clear.
If the chunk boundary cannot be reconstructed, state the scope used.

Use subagents when available, assigning distinct questions relevant to this work.
For example, one can assess agreement with the spec while another examines correctness,
regressions, or the validity of experimental evidence. Choose the number and scope
to fit the work rather than requiring a fixed panel.

Give reviewers the campaign path, relevant files or artifacts, and an explicit
read-only task. They are not alone in the workspace: they must not edit, revert
others' work, or run checks that interfere with other reviewers. Have them return
findings with evidence and limitations. Wait for and reconcile their findings;
do not count unreturned reviews as passes. If delegation is unavailable or fails,
review locally and disclose that the report lacks those independent checks.

Inspect the work and run focused checks within the user's authorization and resource
limits. Reuse relevant recent evidence when it covers the current work. For research,
check the question, comparisons, provenance, analysis, and whether the conclusion
follows from the results. Avoid substituting process compliance for technical review.

Write a readable report under `notes/`, such as `YYYY-MM-DD-chunk-<name>-review.md`;
use a new suffix or a linked follow-up for later rounds. Include:
- The scope and revision reviewed, checks/evidence, and reviewer coverage.
- Findings ordered by impact, each with supporting references and a proposed next action.
- A clear assessment of readiness and what remains unverified.

Confirm findings before presenting them; label uncertain concerns accordingly.
Link the report and actionable follow-up work from `PLAN.md`, preserving other work.
Keep old findings traceable when later checks resolve them. Report when no actionable
issues were found. Review itself does not mark the chunk complete.

For shared report and evidence conventions, see
[the overview](../campaign-start/references/campaign-workflow-overview.md).
