# AI Dev Team

**Clone it, run one command, and get a tailored team of AI agents that builds your idea, remembers what you did, and stops you shooting yourself in the foot.**

---

# Built for people who build by prompting. You bring the idea; the team handles the roles: a product manager to shape it, a lead to plan it, engineers to build it, reviewers to catch problems, and a shared memory so nothing gets forgotten between sessions
---

## Why this exists

One prompt is one context trying to be a product manager, an architect, several engineers, QA, and a reviewer all at once. It works for ten minutes, then the context fills up, the model forgets the plan, and quality falls off a cliff. This splits that work into a small team of focused agents, each with one job and a clean context, plus a living memory so the team stays continuous instead of amnesiac.

## Quick start (Claude Code)

```
git clone <this-repo> my-project
cd my-project
```

Then, in Claude Code, from inside the repo:

```
/project-setup
```

(That's a real slash command this repo adds. You can also just say **set up the dev team** in plain language, which triggers the same thing.)

It sets up the team **right here, in place** — the clone is your project. It reads the templates from `template/`, writes your tailored team into `.claude/`, and gitignores `template/` so the library doesn't ride along in your project's history. It asks, in a sentence, **what you want to build**. If the shape is obvious (a Discord bot, a landing page) it tailors the team to it; if you're not sure yet whether it's a web app, a CLI, or a desktop tool, that's fine and expected: it sets up in **discovery mode** and the product-manager and project-lead help you settle the shape before anything gets built. Want a fresh project later? Just clone again. Two ways to run it:

- **Guided** — it shows you the plan and checks in at key steps. Good if you're newer to this.
- **YOLO** — it makes sensible calls and just builds. Safety checks stay on regardless.

Then:

```
Use the product-manager agent. My idea: <one line>.
```

Approve the plan, and the team takes it from there.

> If `git clone` isn't for you, this isn't your tool. Everything else is built to be beginner-friendly; that one step isn't negotiable.

## Repo layout

This repo is itself a Claude Code bundle, which is why `/project-setup` loads the moment you clone it:

```
ai-dev-team/              clone this; it becomes your project
  .aidevteam             marker the installer anchors on
  template/              the role + skill library (setup reads this; gitignored after setup)
    agents/
    skills/
  .claude/
    skills/project-setup/  the installer (loads on clone)
    commands/            the /project-setup slash command
  README.md  PIPELINE.md  CONTRIBUTING.md  CHANGELOG.md  LICENSE
```

`project-setup` reads the templates from `template/` and writes your tailored team into this repo's `.claude/`, in place.

## What "tailored" means

Not every project needs every role. The setup picks a team from what you're building:

- Building a **CLI tool**? No UI designer, no database engineer, no devops. Lean team.
- Building a **web app with accounts**? You get the database engineer, the UI designer, and devops, each with your actual stack baked in.
- Using **Postgres vs Mongo vs Redis**? The database engineer's rules adapt to your datastore.

Every include and skip is recorded in `.claude/PROJECT_CONTEXT.md` with the reason, so the choices are legible later.

## The team

**Always on:**

| Role | Job |
|---|---|
| `product-manager` | Shapes your idea into something buildable; the user's advocate |
| `project-lead` | Turns that into a delegated plan you approve |
| `developer` | Application logic, APIs, integrations |
| `debugger` | "It's broken, why?" Diagnoses before anyone edits |
| `security-auditor` | Adversarial read-only review; can BLOCK a ship |
| `qa-engineer` | Tests behaviour; never edits app code |
| `docs-writer` | Keeps the README honest so you never ship blank |

**Added when the project needs them:** `ui-ux` (has a UI), `db-engineer` (stores data), `devops` (you manage the deploy).

## Living memory (the part that keeps you sane)

Under `.claude/memory/`, the team maintains three small files it reads before working and updates after:

- **`PLAN.md`** — what's being done and what's next.
- **`DECISIONS.md`** — why you chose things, so nobody re-litigates them.
- **`PROGRESS.md`** — plain-language status: what works, what's half-built, what's broken.

Come back after a week and `PROGRESS.md` tells you exactly where you left off.

## Safety net

The `guardrails` skill catches the costly, avoidable mistakes: committing secrets, working straight on `main`, running a destructive migration with no backup. Setup also generates a `.gitignore` and a `.env.example`. The `smoke-test` skill confirms the thing actually **builds, boots, and loads** before calling anything done. The `pipeline-gate` skill keeps the team from collapsing into one context: no code gets written without an approved plan, so a stray "just build it" gets routed back through the flow instead of bulldozing it. These stay on even in YOLO mode.

## Skills

Auto-activating checklists that keep recurring work consistent: `project-memory`, `pipeline-gate`, `guardrails`, `smoke-test`, `security-review`, `new-endpoint`, `db-migration`, `data-ingestion`, and `new-agent` (for building multi-agent pipelines). Setup includes only the ones your project needs.

## Keeping up to date

Improved an agent upstream, or pulled a newer version of this repo? Run `/project-setup` and say **sync**. It re-applies the latest agents and skills with your recorded stack, and never touches your living memory.

## The six-field anatomy

Every agent is the same shape, so you can read, trust, and adapt any of them fast: **role** (one job) · **instructions** (how it works) · **skills** (scoped capabilities) · **tools** (least privilege) · **context** (its slice of the brief) · **output** (a fixed contract the next role can use).

## Contributing

New roles, skills, and archetypes welcome. See [`CONTRIBUTING.md`](./CONTRIBUTING.md). Keep agents single-purpose, their contexts tight, and the language plain.

## Licence

MIT. Fork it, rename the roles, build your team.
