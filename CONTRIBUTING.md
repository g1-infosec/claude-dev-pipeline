# Contributing

New roles, skills, and archetypes are very welcome. The whole repo is just Markdown, so contributing is mostly writing clear instructions well.

## The shape everything follows

Every agent uses the same six-field anatomy: **role** (one job) · **instructions** (how it works) · **skills** (scoped capabilities) · **tools** (least privilege) · **context** (its slice of the brief) · **output** (a fixed contract). Keep to it.

## Add a role (agent)

1. Create `template/agents/your-role.md` with YAML frontmatter (`name`, `description`, `tools`, `model`) and instructions.
2. One job only. If the role needs "and" to describe it, split it.
3. Least-privilege `tools`. Read-only if it reviews.
4. A fixed output format the next role can consume.
5. Leave a single `<!-- Adapt: ... -->` line for anything stack-specific, so `project-setup` can bake it in.
6. Wire it into `project-setup`: add it to the roster logic and the relevant archetype presets, and to `project-lead`'s delegation table if it's a build role.

## Add a skill

1. Create `template/skills/your-skill/SKILL.md` with `name`, `description` (say when it auto-activates), and `allowed-tools`. (The one exception is `project-setup`, the installer, which lives in `.claude/skills/` so it loads on a clone.)
2. Make it a scoped checklist, not a general essay.
3. Add it to `project-setup`'s skill-selection logic.

## Add an archetype (preset)

1. Add a row to the archetype table in `.claude/skills/project-setup/SKILL.md`: which extra roles and skills it pulls in, and a sensible default stack.
2. Keep the always-on core (product-manager, project-lead, developer, security-auditor, qa-engineer, debugger, docs-writer + project-memory, guardrails, smoke-test) implicit; only list what the archetype adds.

## Keep it agnostic

This repo is domain-free on purpose. Don't hardcode a company, product, stack, or path into an agent's body. Stack specifics go in the `Adapt:` line for `project-setup` to fill. If you're contributing something harvested from a real codebase, strip the domain first.

## Style

- Plain language. The end users are often beginners.
- Short. A skill nobody reads helps nobody.
- Framework-honest: if something uses Claude Code tool names, say so; don't pretend it's universal.
