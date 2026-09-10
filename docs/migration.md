# Moving to Campaign Workflow

Version 2 separates intended work from current state and makes historical retrieval
selective. Existing campaign records do not need a bulk migration. The earlier shared
workflow also replaced the Claude-only kit; those installation notes remain below.

## Moving to the five-record workflow in v2

New campaigns add `STATE.md` for campaign/chunk status, approvals, active restrictions,
evidence pointers, and the next action. `SPEC.md` holds objectives and criteria;
`PLAN.md` describes intended work and changes only when that work changes.
`DECISIONS.md` records significant design/experimental choices. Detailed review and
run reports stay in `notes/`, and `RESULT.md` holds the synthesized outcome and closure
approval. Routine approvals and completion events need no decision entry.

Older campaigns can resume from existing status and handoff sections without writing
new files. Updating installed skills or refreshing instructions does not itself
migrate records. During an authorized documentation update:

1. Inspect existing records and retain valid approvals, their timestamps and scope,
   current restrictions, and useful historical content.
2. Introduce `STATE.md` as the current snapshot and replace previous operational
   sections with a clear pointer. Preserve unique history before removing its only copy.
3. Move accumulated execution narrative and non-design decision entries into linked
   notes, preserving wording, timestamps, and evidence. Repair relative links from
   the new location and leave pointers at the old location. Keep substantive choices
   and intended work in their proper records.
4. Check that current state has one clear home and that a fresh session can find the
   next action and its supporting evidence. Surface conflicts rather than guessing.

Adapt only the selected campaign as needed; preserve other campaigns and established
historical files. See [record access](../skills/campaign-start/references/record-access.md)
for the procedure available inside installed skills.

## Update the installation

For a shared installation that you want to use while editing this kit, run the
README development command with `--dev`. It backs up existing skill copies and
links before connecting the project to the source checkout. This is a one-time
conversion; later refreshes use those links. Plugin users should disable the plugin
for the testing harness before switching to development links.

For a normal copy installation, back up customized skills before replacing them.
The installer without `--dev` refuses to overwrite existing directories. Remove
only the old kit's installed skill directories once backed up, then install the shared
set using the README command.

The old kit shipped these names: `campaign-start`, `campaign-resume`,
`campaign-review`, `campaign-complete`, `chunk-start`, `chunk-review`,
`chunk-complete`; their seven `exp-` counterparts; and `exp-run`, `repo-init`,
`harden`. Later updates also need to account for `campaign-cleanup`.
Do not remove unrelated skills that happen to be installed alongside the kit.
If you customized `harden` independently, keep it as a separate local skill.

Remove the old campaign machinery from your instruction file while preserving
project-specific facts, constraints, and commands. The optional pointer in README
is enough. Old copied guides and `cc_templates/` inside the kit installation are
superseded by the shared overview and assets. Archive local customizations before
retiring those copies.

The old `settings.json` allowlist is not required by this workflow. Leave existing
settings alone unless you deliberately want to edit them; this revision installs
no replacement permissions.

## Moving from duplicate skill copies to links

The installer now uses `.agents/skills/` as the shared storage location, including
for Claude-only installs. Claude discovers relative links to those skills under
`.claude/skills/`. Each skill still has the same name and contents.

If both locations already contain copies, compare and preserve customizations
before replacing them. Back up the kit's installed skill folders in both locations,
then remove only those entries and rerun the installer to get one shared copy and
Claude links. Reapply your customizations to the shared files. Other installed
skills, Claude settings, and campaign records can stay as they are.

For shared project instructions, merge useful content into `AGENTS.md` before
replacing an existing `CLAUDE.md` with a relative link to it. This is separate from
skill installation; the installer leaves project instruction files alone.
Commit both the shared files and their links so fresh checkouts have everything.

## Adding project documentation

The shared setup now includes optional guidance for README.md, a small AGENTS.md,
development and design guides, and standalone notes under `docs/notes/`. Existing
project documents can keep their names and locations. Add or improve them as useful;
there is no required scaffold or new lifecycle for small tasks. Use `repo-init`
for initial or deliberately revisited repo documentation setup. Campaign-start
uses the existing project docs and does not repeat that setup for each campaign.

Campaign work updates affected current guides and links back to its own decisions
and evidence. Keep old campaign records intact. See the
[repository documentation guide](../skills/repo-init/references/repository-documentation.md)
for the convention shipped with the skills.

## Keep historical campaigns readable

Resume campaigns in their existing locations, including
`docs/engineering-campaigns/` and `docs/experiment-campaigns/`.
Preserve branch names, tags, links, and historical approvals. Missing tags or old
headings do not invalidate previous work.

| Previous record or skill | Current home |
| --- | --- |
| Engineering and `exp-` skill pairs | The corresponding shared skill; the spec describes the kind of work. |
| `NOTES.md` | Keep it as a historical note; put new entries in `notes/`. |
| `REVIEW.md` | Keep past reviews; put new review reports in `notes/`. |
| `experiments/` and `exp-run` | Keep old runs; new run notes are part of chunk work and normally live in `notes/`. |
| `RESULTS.md` | Keep existing tables/evidence; create `RESULT.md` when useful and link to them. |
| Legacy `repo-init` | Install skills separately. The new repo-init sets up or refreshes project docs and shared instructions, without Git/settings preflight gates or a mandatory initialization state. |
| `harden` | Ask for focused engineering work; it is outside the campaign lifecycle. |

Avoid maintaining two competing final conclusions: treat an existing `RESULTS.md`
as the current outcome until `RESULT.md` is introduced, then link the old evidence
from the new result and mark which summary is current. Preserve the old file and
its links. Older campaigns do not need new documents solely to resume; add a record
when it has a job to do.

Cleanup can make small evidence-backed repairs as you work. It does not rewrite
historical conclusions or silently mark old campaigns closed.

## Changed defaults

Interviews follow the conversation. Plans can evolve. Chunks target one session,
not one experiment. Runs can be performed by an agent or a human. Run provenance
matters; a tag per run does not.

Agents checkpoint work on working branches. Human involvement is concentrated on
the actual campaign result and closure, main-branch integration, and meaningful tags.
No automatic squash, reset, tag, merge, push, or branch deletion accompanies closure.

The shared skills can be selected from ordinary requests. The old blanket
`disable-model-invocation` setting is removed so the same skills can support
continuation and delegated cleanup across harnesses. Selecting a skill does not
supply missing user intent or bypass approval of a final result.
