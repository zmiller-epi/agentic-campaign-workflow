# Campaign Workflow

A small set of skills for computational research and engineering work that spans
sessions. Claude Code, Codex, and other agents share the same Markdown records.

Start with a conversation, work in session-sized chunks, review the evidence, and
leave enough context for the next session. Engineering, experiments, and mixed
campaigns use the same skills. The plan can change as the work teaches you something.

## The working record

New campaigns default to `docs/campaigns/<name>/`:

```text
SPEC.md          What we want to build or learn, and what would count as success
PLAN.md          Intended chunks, approach, dependencies, and assessment methods
STATE.md         Current status, approvals, restrictions, and the next action
DECISIONS.md     Significant design and experimental choices, with reasons
RESULT.md        Outcome, evidence, limitations, and the user's closure approval
notes/           Working notes, reviews, run records, and other useful context
```

The five files start small; `RESULT.md` stays a draft until there is an outcome.
Headings are prompts to adapt, not a schema to satisfy. Existing campaign folders
and useful records can stay where they are.

Update the plan only when intended work changes. Keep state as one compact snapshot,
and record decisions only for substantive choices such as cancelling a planned test
or changing default parameters. Routine approvals, execution events, and completion
announcements do not need decision entries. Review reports and run details live in
`notes/`; current state links to the applicable evidence and unresolved findings.

Agents read state first and use headings/search for relevant spec/plan sections.
Orientation stops when purpose, status, approval/restrictions, blockers, and next action
are clear. Links point to answers, not a list of files to load. See
[record access](skills/campaign-start/references/record-access.md) for selective retrieval,
bounded historical searches, searchable note summaries, and older campaigns.

Use concise, plain language: facts, decisions and reasons, evidence, uncertainty, and
next actions. New notes use a [short template](skills/campaign-start/assets/NOTE.md)
with a standard summary: event time, chunk/run, affected files/topics, and a 1–2
sentence finding. Agents can search these blocks without a separate notes index.
Aim for about 200 lines or fewer; link large artifacts and preserve history. One coherent
activity can have one note; every action, session, or lookup does not need a new file.

New date stamps include hours, minutes, and a UTC offset: `YYYY-MM-DD HH:mm ±HH:MM`
(for example, `2026-09-08 18:35 -07:00`). Note filenames use
`YYYY-MM-DD_HH-mm±HHMM-topic.md`, such as `2026-09-08_18-35-0700-review.md`.
See the [timestamp convention](skills/campaign-start/references/campaign-workflow-overview.md#timestamps)
for clock and time-zone handling. Existing timestamps and filenames stay intact.

The [workflow overview](skills/campaign-start/references/campaign-workflow-overview.md)
holds the conventions. Agents read it when needed, especially during cleanup.
It is not imported into every session through `AGENTS.md` or `CLAUDE.md`.

## Project documentation and small tasks

For the project using this workflow, a useful starting layout is:

```text
README.md                 # purpose, quick start, and documentation links
AGENTS.md                 # brief agent guidance and pointers
CLAUDE.md -> AGENTS.md     # shared instructions
docs/
  development.md          # setup, common commands, and checks
  design.md               # current architecture, methods, and assumptions
  notes/                  # standalone investigations and small tasks
  campaigns/              # larger efforts and their records
```

Use existing project conventions and create these files only when they have useful
content. Small tasks can leave one optional note; straightforward fixes may need
only a commit and relevant checks. Changes to setup, usage, or design should update
the corresponding project guide and link back to campaign or note evidence as useful.

The [repository documentation guide](skills/repo-init/references/repository-documentation.md)
explains the roles and how they fit together. Repo-init sets up or refreshes these
docs; campaign-start uses the existing context for each new campaign. Completion
skills maintain affected guides, and campaign cleanup flags stale guidance for the
parent to address. The installer itself leaves project docs alone.

## The skills

| Skill | Purpose |
| --- | --- |
| `repo-init` | Establish useful project docs and shared agent instructions; revisit explicitly when repo setup needs attention. |
| `campaign-start` | Clarify objectives and assumptions, obtain approval of the spec and plan, and hand off execution to a fresh session. |
| `chunk-start` | Get oriented and begin implementing or investigating the next chunk. |
| `chunk-review` | Use independent subagents to review the work and write a report in `notes/`. |
| `chunk-complete` | Record evidence, update and clean up docs, checkpoint the work, and stop with a session handoff. |
| `campaign-review` | Use independent subagents to review the whole campaign and write a report in `notes/`. |
| `campaign-complete` | Draft the outcome, run cleanup, obtain approval, close the campaign, and end the session's work. |
| `campaign-resume` | Inspect the current state, orient the user, and pause for their next direction. |
| `campaign-refresh` | Reread updated workflow instructions in the current task; optionally pull the shared development source. |
| `campaign-cleanup` | Tidy the record and surface consequential discrepancies. Usually delegated. |

For a fresh project, `repo-init` can prepare the documentation before the first
campaign. Existing projects can start a campaign directly. Setup is optional and
safe to revisit; each campaign reuses the project docs rather than repeating setup.

A typical campaign starts with an interactive planning session using `campaign-start`.
After the user approves the documents, the agent records approval and stops, suggesting
clearing context or starting a new session. Each working session covers one chunk:
`chunk-start → work → chunk-review → chunk-complete`. Completion updates the documents
and stops with a prompt for the next session; it never starts the next chunk. After
the final chunk, a later session can run `campaign-review → campaign-complete`, which
also ends with a fresh-session suggestion before any follow-up work.

Handoffs in `STATE.md` carry the next action, essential evidence links, valid approvals,
and active restrictions across sessions. Each handoff replaces the current snapshot;
useful history stays in linked notes. Resume wherever useful. Review can uncover another chunk; cleanup
does not enforce a rigid sequence. Small tasks do not need to become campaigns.

Delegation also applies during planning and execution. Keep intent, decisions, and
tightly coupled work in the main session; hand off bounded investigations, separate
implementation tasks, verification, or documentation when useful work can proceed
independently or a broad search would consume the main context. See
[work allocation](skills/campaign-start/references/work-allocation.md) for ownership
and compact handoffs. Small direct tasks can stay local.

Reviews delegate detailed inspection and checks to independent subagents; the calling
session scopes the work and synthesizes compact findings into a report. If delegation
is unavailable, record the review gap and hand off to a dedicated review session instead
of filling the current context with the review. Cleanup receives documentation ownership
only and can run locally when delegation is unavailable. Routine cleanup starts with
the chunk's affected records and links, expanding when discrepancies warrant it;
closure reconciles the accumulated outcome. Cleanup also replaces duplicated current
prose with source links and makes long notes easier to navigate, preserving historical
evidence. No custom subagent registration is required.

## Install

The same skill directories are used by both harnesses. The installer and optional
development refresh helper require Python 3.9+. The campaign workflow otherwise
uses Markdown instructions, with no hooks, services, or permission configuration.

From this checkout:

```bash
python3 scripts/install.py --project /path/to/your/project --harness both
```

The installer keeps one copy of each skill in `.agents/skills/`. With
`--harness both` or `--harness claude`, it creates a relative symlink for each skill
under `.claude/skills/`, pointing to that shared copy. `--harness codex` installs
only the shared files.

```text
your-project/
  .agents/skills/campaign-start/          # the actual skill files
  .claude/skills/campaign-start           # -> ../../.agents/skills/campaign-start
```

Edits to an installed skill are immediately shared between both harnesses.
The installer uses individual skill links so other Claude skills and settings can
coexist. The default copy mode refuses to replace existing copies or links, and
leaves project instruction files, settings, and campaign records alone. Changes in this kit's
source checkout still require updating the installed files.

Relative links remain valid when a project is moved or checked out in another
worktree. On Windows, symlink creation requires Developer Mode or appropriate
privileges; use plugin installation if symlinks are unavailable.

- Codex discovers project skills under `.agents/skills/`; invoke
  `$campaign-start`. See [Codex skill documentation](https://learn.chatgpt.com/docs/build-skills).
- Claude Code discovers project skills under `.claude/skills/`; invoke
  `/campaign-start`. See [Claude Code skill documentation](https://code.claude.com/docs/en/skills).
- Other harnesses can load the same `SKILL.md` files directly. Copy all the skill
  directories together so their relative links remain usable. Ask the agent to
  read a skill if its harness has no skill discovery.

Start a fresh session if newly installed skills are not visible. Keep installed
skills versioned with the project if its worktrees should inherit them; otherwise
install them in each checkout that needs them.

### Develop skills across projects

While editing this kit, connect each test project to the same source checkout once:

```bash
python3 scripts/install.py --project /path/to/your/project --harness both --dev
```

Then, in a project task, say:

> Refresh campaign skills, then continue.

Or, to fetch upstream updates first:

> Pull the latest campaign skills and refresh, then continue.

You can also invoke `$campaign-refresh` in Codex or `/campaign-refresh` in Claude.
If the current task has not discovered the new skill yet, ask it to read
`.agents/skills/campaign-refresh/SKILL.md` directly and follow it.

Development mode links each `.agents/skills/<name>` to this checkout's `skills/<name>`;
Claude links still point to those shared project entries. All linked projects on this
machine see saved source edits, including uncommitted changes and branch switches.
Rerunning `--dev` is safe: correct links stay in place, new skills get links, and
obsolete links into this source are retired. Other installed skills are preserved.
Refresh stops on a conflicting local skill; only an explicit installer conversion
backs up and replaces an existing copy.

Keep this source checkout at a stable location; rerun the installer from its new
location if you move it. Each machine needs its own checkout and development setup.

When converting an existing copy installation, `--dev` preserves replaced skill
folders and links under `.agents/campaign-workflow-backups/dev-<unique-id>/`, outside
skill discovery. The backup mirrors the original project paths and is printed by the
installer. Customizations remain in that backup; compare and deliberately apply any
shared changes to the source. An installation failure restores the replaced entries.
Project instructions, settings, campaign records, and unrelated skills stay intact.

For plugin-installed test projects, disable the Campaign Workflow plugin for that
harness before using development links so there is one active copy of the skills.
The installer does not change plugin installations. Development links contain local
absolute paths; keep them local rather than committing them for other machines.
The default copy installation and plugin packaging remain useful for distribution.

A plain refresh is local and performs no fetch. A requested pull fast-forwards the
source checkout's current branch from its configured upstream, normally `main`.
Use a source checkout tracking `main` when that is the version you want to test.
Dirty, detached, missing-upstream, or divergent source states stop the pull; local
refresh still works. Refresh never switches branches, stashes edits, or changes the
consuming project's Git history. It resynchronizes development links after the pull.

The helper can also be run directly from the consuming project root:

```bash
python3 .agents/skills/campaign-refresh/scripts/refresh.py --project .
python3 .agents/skills/campaign-refresh/scripts/refresh.py --project . --pull
```

It reports the source revision, local edits, files changed by a pull, and paths to
reread. The agent then rereads the overview and instructions needed for the current
action before continuing. This updates the instructions used in the current task;
it does not guarantee that a harness refreshes its skill/tool catalog mid-session.
Campaign records and prior work remain in place. Any material change to the campaign
plan still needs user approval.

### Plugin packaging

This checkout also includes `.claude-plugin/plugin.json` and
`.codex-plugin/plugin.json`, both pointing to the same skills. For a local Claude
Code session, run `claude --plugin-dir /path/to/agentic-campaign-workflow`, then invoke
`/campaign-workflow:campaign-start`. See the
[Claude plugin reference](https://code.claude.com/docs/en/plugins-reference).
Codex can use the direct skill installation above; the manifest is included for
plugin distribution. This repository does not register a marketplace or change
your global installation.

Choose one installation route per harness to avoid duplicate skill entries.
Skills can be selected from ordinary requests as well as invoked by name; user
intent and the final approval boundary still govern what they do.

### Optional project pointer

The workflow works without adding anything to a project's instruction files.
If a pointer helps discovery, add a few lines to its existing `AGENTS.md` or
`CLAUDE.md`, adjusting the overview path to the installation:

```markdown
Campaigns normally live in docs/campaigns/.
Use docs/notes/ for standalone findings worth preserving.
Use the campaign skills when working on one. Read
.agents/skills/campaign-start/references/campaign-workflow-overview.md
when workflow context is useful. Keep campaign details in the campaign folder.
```

Use the same `.agents/skills/` path for Claude-only installation: it is the shared
storage location there too.

To share project instructions, keep them in `AGENTS.md` and make `CLAUDE.md` a
relative symlink to it. This repository uses that arrangement. In a project that
already has `AGENTS.md` and has no `CLAUDE.md`, run from the project root:

```bash
ln -s AGENTS.md CLAUDE.md
```

If both instruction files already exist, reconcile any distinct content before
replacing either. The installer does not do that merge or create this link for you.
For Claude-specific additions, use a regular `CLAUDE.md` containing `@AGENTS.md`
followed by those additions. Both sharing approaches are documented by
[Claude Code](https://code.claude.com/docs/en/memory#agentsmd).

Keep project facts in the project's own instruction files. Do not copy this
repository's `AGENTS.md` into another project: it describes maintaining the kit itself.

## Git defaults

Make frequent, focused checkpoint commits on working branches. Use worktrees for
concurrent work. Reuse an appropriate existing branch and follow project naming;
there is no required branch prefix, squash strategy, per-chunk tag, or clean-main
starting ritual.

The human controls integration into the main branch and meaningful milestone or
release tags, including the proposed message. Closing a campaign records its
outcome; merging, pushing, publishing, and deleting branches are separate actions.
Record experiment code revisions and input/configuration provenance in notes,
so reproducibility does not depend on tags.

## Moving from the previous kit

Read [migration notes](docs/migration.md) before updating an existing installation.
Version 2 separates current state from planned work and limits decision entries to
significant design/experimental choices. Older campaigns remain readable, and existing
history is preserved during an authorized adaptation. The engineering and `exp-` skill
pairs have been consolidated. The current
`repo-init` is optional documentation setup; the old kit's Git and installation
preflight requirements do not apply. `exp-run` and `harden` are no longer separate
workflow skills.

## Maintaining this repository

Run the installer checks with:

```bash
python3 -m unittest discover -s tests -v
```

They exercise both installation layouts, preservation of existing files, and
relative references. The skills themselves are instructions; structural checks
cannot establish how well an agent interviews, investigates, or reviews.
