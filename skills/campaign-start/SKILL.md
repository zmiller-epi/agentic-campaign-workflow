---
name: campaign-start
description: Start an engineering, experiment, or mixed campaign through a conversational interview, relevant context gathering, and a shared spec and plan.
---

# Start a campaign

Use the user's request and conversation as the starting point. Interview them about
what they want to build or learn, asking whether this is engineering, an experiment,
or a mixture. If they have already said, acknowledge it and ask the next useful
question. Use a question tool when available, or ask in conversation, in small rounds.

Explore the relevant project and previous campaigns as the conversation develops.
Use what you learn to clarify the intended outcome, uncertainty, and tradeoffs.
Probe consequential assumptions in both the request and your proposed approach: what
must be true for the work to be useful, what evidence supports it, and what would
change the direction. Distinguish confirmed facts from assumptions to validate.

Work with the user to define concrete campaign completion criteria. Translate vague
goals into observable outcomes and the checks, measurements, or artifacts that will
establish them, including thresholds or acceptance examples where useful. For research,
clarify what evidence is sufficient to stop and how negative or inconclusive results
will be judged; completion need not depend on confirming the hypothesis.

Follow the user's answers instead of a fixed checklist; do not ask them to repeat
facts already available. Stop interviewing when there is enough shared understanding
to draft a spec and plan for approval, including completion criteria and consequential
assumptions. Resolve unknowns that would change the goal or criteria, or explicitly
propose how the plan will investigate them. Other details can remain open questions.
Do not invent interview answers while waiting for input.

Read [the overview](references/campaign-workflow-overview.md) when establishing
the workflow or resolving a convention. It provides context, not extra interview gates.

Use existing project documentation as context. Repository-wide setup belongs to
[repo-init](../repo-init/SKILL.md); do not repeat it for every campaign or invoke it
automatically because a suggested file is missing. If setup would help, mention it
while continuing the campaign work that is already clear. No initialization marker
or complete set of project docs is required.

Summarize the intended campaign and make consequential assumptions visible. Choose a
clear name and use `docs/campaigns/<name>/` unless the project has another convention.
If that campaign exists, inspect it and clarify whether to resume rather than overwrite.
Reuse an appropriate working branch, or create one following project/harness conventions.
Preserve existing changes; a dirty tree does not prevent interviewing or drafting.

Adapt the templates in [assets](assets) into the campaign folder:

- [SPEC.md](assets/SPEC.md): purpose, kind, scope, completion criteria, assumptions, and open questions.
- [PLAN.md](assets/PLAN.md): session-sized chunks, with the next chunk concrete and later work rough.
- [DECISIONS.md](assets/DECISIONS.md): decisions already made and their reasons; otherwise a brief empty log.
- [RESULT.md](assets/RESULT.md): a draft placeholder for the eventual outcome.
- `notes/`: an initially empty folder for working notes, run records, and reviews.

Keep the spec suitable for the work: engineering behavior, research question and
comparisons, or both. Plan around outcomes, not one run per chunk. Include relevant
prior-campaign links and where the next session should begin. Drop unhelpful template
prompts instead of filling them with boilerplate.

Keep the campaign status draft while preparing the spec and plan and awaiting
user approval. Make a focused checkpoint commit of the draft records on the working
branch when Git is available. Show the user the spec, plan, completion criteria,
consequential assumptions, unresolved choices, and proposed next chunk, and ask for
approval of that plan.

**Do not begin implementation, experiments, or other campaign chunks until the user
explicitly approves the presented plan.** Interviewing, read-only context gathering,
and drafting or revising campaign records may continue before approval. A request to
start a campaign or to proceed is not approval of a plan the user has not seen; silence
is not approval either. Reuse approval already given for the unchanged plan. If a
revision materially changes the proposed scope, approach, or completion criteria,
show the revision and obtain approval before executing it.

After approval, record it and the date in `PLAN.md`, set the campaign status to active,
and proceed with the approved next chunk when execution is within the user's request.
