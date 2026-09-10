# Campaign Workflow v2 validation

**Created:** 2026-09-09 17:11 -07:00
**Scope:** Shared skills, templates, guides, and plugin metadata on
`codex/campaign-v2`, based on `origin/main` at `a32dd86`. Both plugin manifests use
version `2.0.0`; the requested release tag is `v2`.

## Automated checks

- `python3 -m unittest discover -s tests -v`: all 28 tests passed. These cover copy
  and development installs, shared assets, both harness paths, preservation, relative
  references, and local Git refresh behavior.
- The skill-creator `quick_validate.py` validator passed for all 10 skill entrypoints.
- All 75 relative documentation links checked in README, migration guidance, and
  shared skills resolve. Both plugin manifests point to the shared skills directory.
- `git diff --check` passed before release preparation.

## Forward tests

Independent agents received realistic requests and minimal temporary fixtures,
without expected routing answers. The fixtures were outside the source repository;
no existing user campaign or external experiment was modified.

| Scenario | Observed outcome |
| --- | --- |
| Execute and complete an unchanged planned run | One deterministic simulation produced JSON with sum 45 and count 10. Independent assessment passed. The completed fixture changed only existing `STATE.md` and added one run note/output artifact. Spec, plan, decisions, draft result, reviewed script, and review were byte-for-byte unchanged. Approval and the consumed one-run limit remained in state. |
| Adapt an older campaign | Cleanup created state, preserved approval scope/timestamps and one-run/no-network restrictions, moved routine history into a linked note, and retained the substantive filter decision. Parent assertions checked historical passages, untouched result/review/artifact bytes, and all 19 local links and fragment anchors. |
| Repeat routine cleanup | The second pass reported no meaningful issue. A before/after inventory and SHA-256 comparison confirmed no file, content, or in-file timestamp changes. |
| Retrieve a superseded historical finding | The retrieval agent read two substantive notes among 82 notes and returned the corrected method-A range through alpha 0.9, leaving alpha 1.0 unverified. It identified the original input-conversion error, supersession, and lack of raw-output verification. The fixture remained unchanged. |
| Change a default and cancel a planned test | The agent changed the planned seed count from 3 to 5, removed the optional dense-grid chunk, and recorded the substantive budget rationale. Spec/state were reconciled; approval history and resource restrictions were preserved. The draft result stayed unchanged and no experiments ran. |

The retrieval test initially emitted matching snippets from 80 irrelevant benchmark
notes because its query was too broad, although it did not read those files in full
or load them into the parent. The shared procedure was refined to prefer filename-only
matches or bounded snippets and narrow broad queries before returning large results.
The final refinement received static review; no token-savings claim is made.

The routine-execution test required parent assistance: automatic approval review did
not recognize fixture-write authorization in the minimal-context worker task. After
the worker's blocked attempts, the parent executed the single simulation under the
root user's test authorization and persisted the worker's proposed completion records.
The worker independently assessed the actual output; the parent verified the final
file changes and links. Worker-side persistence and the initial in-progress state
transition were not demonstrated. Unknown invocation time/interpreter details were
kept unknown in the fixture record rather than inferred.

## Independent source review

A read-only reviewer inspected all 19 tracked source changes and the two new shared
resources, including the final retrieval refinement. It reported no actionable
contradictions in record ownership, review routing, authorization preservation,
selective access, or legacy adaptation. This was static review, separate from the
forward tests and installer checks.

## Limits

The behavioral checks are small synthetic examples on the available agent harness.
They do not establish behavior on every harness, in long production campaigns, or
under every authorization configuration. No comprehensive token benchmark or costly
scientific rerun was performed. Packaging/link checks and observed agent behavior
are reported separately above.
