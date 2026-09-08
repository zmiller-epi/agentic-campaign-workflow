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
Follow the user's answers instead of a fixed checklist; do not ask them to repeat
facts already available. Stop interviewing when there is enough shared understanding
to write a useful initial spec and begin the next chunk. Unresolved details can
remain explicit questions. Do not invent interview answers while waiting for input.

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

- [SPEC.md](assets/SPEC.md): purpose, kind, scope, success evidence, and open questions.
- [PLAN.md](assets/PLAN.md): session-sized chunks, with the next chunk concrete and later work rough.
- [DECISIONS.md](assets/DECISIONS.md): decisions already made and their reasons; otherwise a brief empty log.
- [RESULT.md](assets/RESULT.md): a draft placeholder for the eventual outcome.
- `notes/`: an initially empty folder for working notes, run records, and reviews.

Keep the spec suitable for the work: engineering behavior, research question and
comparisons, or both. Plan around outcomes, not one run per chunk. Include relevant
prior-campaign links and where the next session should begin. Drop unhelpful template
prompts instead of filling them with boilerplate.

Set the campaign status to active once the initial direction is established; leave
it draft if the interview is still waiting on a consequential answer.
Make a focused checkpoint commit on the working branch when Git is available.
Show the user the spec, plan, unresolved choices, and proposed next chunk.
This skill establishes the campaign; begin implementation only when the user's
request also asks to proceed.
