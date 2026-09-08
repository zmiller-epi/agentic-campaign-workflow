# Moving to Campaign Workflow

This revision replaces the Claude-only kit with eight shared skills. Existing
campaign records do not need a bulk migration.

## Update the installation

Back up any customized installed skills before replacing them. The installer refuses
to overwrite existing directories. Remove only the old kit's installed skill
directories once backed up, then install the shared set using the README command.

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
there is no required scaffold or new lifecycle for small tasks.

Campaign work updates affected current guides and links back to its own decisions
and evidence. Keep old campaign records intact. See the
[repository documentation guide](../skills/campaign-start/references/repository-documentation.md)
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
| `repo-init` | Install skills, then let campaign-start create the campaign folder as needed. |
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
