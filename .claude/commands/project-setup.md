---
description: Set up a tailored AI dev team in this repo, in place (runs the project-setup skill).
---

Use the **project-setup** skill to stand up a tailored AI dev team **in place** — the clone is the project. It reads templates from `template/` and writes your tailored team into this repo's `.claude/`. Don't ask which project to target; it's this one, unless the user explicitly names another path.

Start from the user's idea, not an architecture choice. Follow the skill's phases: Mode → Idea → Shape (infer it if it's clear, otherwise defer to discovery mode) → Intake (only if the shape is known) → Selection → Generation.

If the user only has a fuzzy idea, and isn't sure yet whether it's a web app, a CLI, or a desktop tool, that is the normal case: use discovery mode. Install the team, leave the stack as `to be decided`, seed the idea into `.claude/memory/`, and hand off to the product-manager. The shape gets decided in the project-lead's brief and locked in on approval.

Anything the user typed after the command is their idea or the target path; use it:

$ARGUMENTS
