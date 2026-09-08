---
name: campaign-complete
description: Prepare a campaign's final result, obtain user approval of the concrete outcome, and close or abandon it with documentation cleanup.
---

# Complete a campaign

Resolve the campaign and intended disposition: completed, abandoned, or paused.
Read its spec, plan, decisions, evidence, and relevant reviews. Missing ceremonies
do not by themselves block closure, but unsupported claims and unresolved substantive
findings need honest treatment. A negative or inconclusive experiment may still
fulfill the campaign's objective.

For older campaigns, read the existing `RESULTS.md` or other outcome record first.
Preserve it as evidence and link it from the new result so there is one current summary.
Prepare `RESULT.md` using the [template](../campaign-start/assets/RESULT.md) when useful.
Explain what was built or learned, the evidence, limitations, unresolved work, and
what should happen next. For abandonment, say why the work stopped and what remains
worth keeping. For a pause, retain an open status and a concrete resume action.
Keep the result marked draft while preparing it. Do not fill approval from inference.

Reconcile affected project guides with what the campaign actually delivered or learned,
following the [repository documentation guide](../repo-init/references/repository-documentation.md)
where useful. Preserve the campaign's reasoning and evidence and link to them; label
pending conclusions and do not present abandoned approaches as current project behavior.

Run [campaign-cleanup](../campaign-cleanup/SKILL.md), preferably in a subagent,
before presenting the final draft. Give it the campaign path and documentation-only
ownership; it is not alone in the workspace and must preserve others' edits. Do not
edit those same documents concurrently. Wait for it and inspect the result; perform
the same pass locally if delegation is unavailable. Resolve meaningful discrepancies.

Show the user the concrete `RESULT.md`, proposed closure status, evidence, and remaining
limitations. **Obtain approval of this result and disposition before marking the campaign
closed.** A request to run this skill is not approval of an unseen result. Prior approval
of this exact outcome is sufficient; do not ask again unless it materially changed.
While approval is pending, leave campaign status open and the result draft.
If the user requests changes, revise and present the changed result.

After approval, record the approval and date in `RESULT.md`, update the campaign status
in `SPEC.md`, and reconcile `PLAN.md`: distinguish finished, deferred, and dropped work.
Checkpoint these documents on the working branch. If closing introduces only status
or link edits, a short local consistency check suffices; do not repeat a full review.

Campaign closure does not require integration. If the user also requested merging
or meaningful tags, prepare the exact content and proposed message and use their
specific authorization for those actions. Do not infer permission to merge, push,
publish, delete branches, or rewrite history from closure approval.

Report the outcome and link the result and main review. Distinguish the campaign's
closure from any Git integration still pending.
See [the overview](../campaign-start/references/campaign-workflow-overview.md)
for shared conventions.
