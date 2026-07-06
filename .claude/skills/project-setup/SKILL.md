---
name: project-setup
description: Sets up a tailored AI dev team in the cloned repo itself — you edit in place, so the clone becomes your project. Run it from inside the repo. Activates on "set up the dev team", "set up my project", "configure the agents", "/project-setup", or "vibe setup". Starts from your idea (not an architecture choice): it infers the shape when it's clear, or defers it to the product-manager and project-lead when it isn't, then copies tailored agents and skills from template/ into .claude/ and seeds living-memory files.
allowed-tools: [Read, Write, Glob, Grep, Bash]
---

# Project Setup

You stand up a bespoke AI dev team for a project by tailoring the generic agents and skills in **this repo**. The person running this may be a "vibecoder": they build by prompting, may not know the jargon, and want to get building fast. Meet them there. Infer aggressively, ask little, explain in plain language, and never leave them with a half-configured mess.

Phases: **Mode → Idea → Shape (infer, or defer to discovery) → Intake (only if the shape is known) → Selection → Generation.** In guided mode you confirm before writing. In YOLO mode you skip the confirm but never skip the safety files.

---

## Locating the library and the target

You **edit in place**: the cloned repo becomes the user's project. There is no separate source repo and target to keep apart.

- **Library = `<repo>/template/`.** Resolve `<repo>` once: the directory whose root holds the `.aidevteam` marker (search upward from where the skill is running). The generic role and skill templates live in `<repo>/template/agents` and `<repo>/template/skills`. Read from there; never modify them.
- **Target = the repo itself, in place (the default).** Write the tailored team into `<repo>/.claude/`. Don't ask "which project?" — the answer is "this one". `project-setup` already lives in `<repo>/.claude/skills/`; leave it there.
- **Only ask for a path if the user wants the team somewhere else** (e.g. a specific package of a monorepo). Then treat that path as the target and write its own `.claude/` there. Otherwise, in place.

### Monorepo

If the repo has multiple apps/packages with different stacks, offer to set up at a chosen subdirectory (each can have its own `.claude/`), or at the root for the whole thing. Default to the root, in place, unless the user picks a package. Never treat `template/` as an app to configure.

### Not a git repo

That's fine, you still write `.claude/`. The guardrails will suggest `git init` later.

---

## Phase 0 — Mode

Ask once, plainly:

> **How do you want to work?**
> - **Guided** — I'll show you the plan and check in at key steps. (Recommended if you're newer to this.)
> - **YOLO** — I'll make sensible calls and just build. Less talking. (Safety checks still stay on.)

Default to **guided**. In YOLO you still run the `guardrails` skill: secrets and data-loss protection are seatbelts, not gates, and never get turned off.

---

## Phase 1 — Idea, then shape

Start with the idea, not the architecture. Ask the one thing everyone can answer:

> **In a sentence or two, what do you want to build or do?**

Then work out the **shape** yourself (web app, API, CLI, desktop app, bot, and so on) from the idea. Do not make the user pick an architecture they haven't decided yet.

- **Shape is clear from the idea** ("a Discord bot that…", "a CLI that renames files", "a landing page for…") → infer the archetype, say which one you inferred and why, and proceed. Confirm; don't interrogate.
- **Shape is genuinely open** (e.g. "a platform that does external scans" — could be SaaS, a local CLI, or a desktop app, with or without a database) → **do not force a choice.** Deciding that is exactly what the team is for. Go into **discovery mode** below; the shape gets decided during the pipeline and locked in when the user approves the brief.

A user who knows only the idea is the normal case, not an error. Picking the architecture is the team's first job, not the price of admission.

### Discovery mode (shape deferred)

When the shape is open:
- Install the always-on core plus `product-manager` and `project-lead`, and include the conditional roles (`ui-ux`, `db-engineer`, `devops`) as **available**. A dormant role is cheaper than a missing one; Finalise (Phase 4) prunes whatever the chosen shape doesn't need.
- **Don't bake a stack.** Leave each agent's stack as `to be decided`, and record `Archetype: undecided (discovery)` in `PROJECT_CONTEXT.md`.
- Seed the idea verbatim into `.claude/memory/` (the PLAN "Now" item and `PROJECT_CONTEXT.md`) so the product-manager starts from it without the user retyping.
- Skip Phases 2–3 and hand straight to the product-manager. The project-lead's brief then recommends the shape and stack with reasons; approving it triggers Finalise.

### Archetype presets (when the shape is known or inferred)

Always included for every archetype: `product-manager`, `project-lead`, `developer`, `security-auditor`, `qa-engineer`, `debugger`, `docs-writer`, and the skills `project-memory`, `guardrails`, `smoke-test`, `pipeline-gate`.

| Archetype | + Roles | + Skills | Default stack (confirm) |
|---|---|---|---|
| Web app | ui-ux, db-engineer, devops | security-review, new-endpoint, db-migration | modern web framework + a relational DB |
| Landing / static | ui-ux | — | static site generator or plain HTML/CSS |
| API / service | db-engineer*, devops | security-review, new-endpoint, db-migration* | a backend framework + a datastore |
| CLI tool | — | — | the user's preferred language |
| Bot | db-engineer*, devops | security-review, data-ingestion*, db-migration* | a bot framework + light storage |
| Browser extension | ui-ux | security-review | extension APIs + a bundler |
| Mobile app | ui-ux, db-engineer*, devops | security-review | a cross-platform or native mobile framework |
| Data / ML / script | db-engineer* | data-ingestion, new-agent* | the user's preferred language |

`*` = include only if the follow-up confirms it (persists data / ingests feeds / runs a multi-step AI pipeline).

---

## Phase 2 — Intake (only the gaps)

**In discovery mode, skip this phase.** The stack, data, and deploy questions below are decisions the product-manager and project-lead will make with the user during the pipeline; asking them here would re-create the premature-commitment problem. Run intake only when the shape is known or inferred.

Read the target repo first (Glob/Grep) to infer language, framework, datastore, and test runner. Then ask **only** what the archetype and the repo didn't already settle. Every question is plain-language with a "not sure" default:

- **Stack:** "What are you building it with?" → if unsure, propose the archetype default and move on.
- **Data (if role in doubt):** "Does it need to remember things between visits (accounts, saved data)?" Yes → `db-engineer` + `db-migration`. "What kind of storage?" → if unsure, default relational.
- **Feeds (data/bot/service):** "Does it pull in data from other services on a schedule?" Yes → `data-ingestion`.
- **Deploy:** "Where will it live once it's done?" (a host you manage → `devops`; a place like Vercel/Netlify that handles it → `devops` in light mode or skip). If unsure, keep `devops` and note it.
- **Pipeline (data/ML):** "Does it run several AI steps in a row?" Yes → `new-agent`.

Never ask more than a few. If the user shrugs, take the archetype defaults and note the assumptions.

---

## Phase 3 — Selection & confirm

Resolve the final roster from the archetype + answers. **Guided mode: show the plan and wait for "go."** YOLO mode: show it as a one-line summary and proceed.

```
Target: <path>   Mode: guided
Building: Web app  ·  Stack: <stack>

Team:  product-manager, project-lead, developer, ui-ux, db-engineer,
       security-auditor, qa-engineer, debugger, docs-writer
Skills: project-memory, guardrails, smoke-test, pipeline-gate, security-review, new-endpoint, db-migration
Skipped: devops — you're deploying to a managed host that handles it

I'll also add: living-memory files, a .gitignore, and a .env.example.
Reply "go", or tell me what to change.
```

**Discovery mode** (shape deferred) looks like this instead:

```
Target: <path>   Mode: guided
Building: <the idea, verbatim>  ·  Shape: to be decided with the team

Team:  product-manager, project-lead, developer, security-auditor,
       qa-engineer, debugger, docs-writer
Available if the shape needs them:  ui-ux, db-engineer, devops
Skills: project-memory, guardrails, smoke-test, pipeline-gate
Stack:  to be decided (the project-lead's brief will recommend one)

Next: I'll hand your idea to the product-manager to shape it. You'll
approve a definition, then a plan, and then the team builds.
Reply "go" to set this up.
```

---

## Phase 4 — Generation

On approval (or immediately, in YOLO):

1. **Create** `<target>/.claude/agents/`, `<target>/.claude/skills/`, and `<target>/.claude/memory/`. (Editing in place, `<target>` is `<repo>`.)
2. **Agents:** for each chosen role, read `<repo>/template/agents/<role>.md`, replace its `<!-- Adapt: ... -->` line with the concrete stack (see below), and write to `<target>/.claude/agents/<role>.md`.
3. **Skills:** copy each chosen skill from `<repo>/template/skills/<skill>/SKILL.md` to `<target>/.claude/skills/<skill>/SKILL.md`. Always include `project-memory`, `guardrails`, `smoke-test`, `pipeline-gate`. (`project-setup` already lives in `.claude/skills/` and isn't in `template/`; leave it alone.)
4. **Prune delegations:** in `project-lead` (and anywhere else), remove references to any role you didn't generate, so it never delegates to a missing agent.
5. **Seed living memory** in `.claude/memory/`:
   - `PLAN.md` — a starter with the user's idea as the first "Now" item.
   - `DECISIONS.md` — seeded with the setup decisions (archetype, stack, roster) and their reasons.
   - `PROGRESS.md` — "Fresh project. Nothing built yet. Next: <first task>."
   - `BRIEF.md` — seeded with `Status: NONE` and a note that the `project-lead` fills this in and the user approves it before any build. The build agents refuse to write code until it says `Status: APPROVED`.
6. **Seed safety files** at the target root:
   - `.gitignore` — create or update it to exclude `template/` (the library shouldn't ride along in the user's project history), plus secrets/`.env`, dependencies, and build output for the chosen stack. If the repo still tracks `template/` from the clone, offer to run `git rm -r --cached template` so the ignore actually takes effect.
   - `.env.example` — keys only, no values, for any secrets the stack implies.
7. **Write** `.claude/PROJECT_CONTEXT.md` — archetype, mode, stack, the full roster with an include/skip reason for each, and any assumptions made. This is the shared context every agent reads. In discovery mode, set `Archetype: undecided (discovery)` and `Stack: to be decided`; Finalise updates these once the brief is approved.
8. **Report:** the roster, the skills, the safety files, and the one-line next step: `Use the product-manager agent. My idea: ...`. In discovery mode, the idea is already seeded, so hand straight to the product-manager to shape it — the shape and stack get decided in the brief, then Finalise locks them in.

### Baking the stack

Replace each agent's single `<!-- Adapt: ... -->` line with the real value, e.g.:
- `developer` → `**Stack:** TypeScript / NestJS / Zod / Jest.`
- `db-engineer` → `**Stack:** Postgres / Prisma / Prisma Migrate.`
- `devops` → `**Environment:** managed host (Vercel) — deploy is handled; focus on config and env.`
- `ui-ux` → `**Stack:** React + Tailwind.`
- `product-manager` → the product one-liner, its audience(s), and its core value.

Unknown value → write `to be decided` and note it in `PROJECT_CONTEXT.md` so the agent asks before assuming. Leave **no** `Adapt:` comments in generated files.

### Finalise (locking in a deferred shape)

When setup ran in **discovery mode**, the shape and stack are decided later, in the project-lead's Implementation Brief. Once the user approves that brief:
1. **Bake the stack** into every agent's `Adapt:` line from the brief (same as Baking the stack above).
2. **Prune** the conditional roles the chosen shape doesn't need, using the archetype presets as the guide, and prune `project-lead`'s delegations to them.
3. **Update `PROJECT_CONTEXT.md`**: set the decided archetype and stack in place of `undecided (discovery)`, with a one-line reason.
4. Never touch `.claude/memory/` history while doing this. This reuses the **sync** machinery: it re-bakes and prunes, it doesn't reset the project.

Trigger Finalise on brief approval, or when the user says "finalise the team" / "lock in the stack".

### db-engineer by datastore type
- **Relational** (Postgres/MySQL/SQLite): keep migration / index / N+1 / parameterised-query rules as written.
- **Document** (Mongo/Firestore): swap "migrations" for schema-versioning + backfill; keep index/query guidance; drop foreign-key assumptions.
- **Key-value / cache** (Redis): drop migrations and joins; focus on key design, TTLs, eviction.

Record which variant you applied.

---

## Sync (updating an existing setup)

If `.claude/agents/` already exists and the user says "sync" or "update the team":
- Re-read `PROJECT_CONTEXT.md` for the recorded archetype and stack.
- Re-copy the chosen agents/skills from `template/`, re-baking the same stack.
- **Preserve** `PROJECT_CONTEXT.md` and everything in `.claude/memory/` (never overwrite the living memory).
- Report what changed.

If it exists and the user is setting up fresh, ask: reconfigure (re-interview) or add/remove specific roles. Never blindly overwrite.

---

## Rules

- **Edit in place by default.** The clone is the project; write the tailored team into this repo's `.claude/`, reading templates from `template/`. Only target a different path if the user explicitly asks.
- **Infer first, ask least.** Read the repo before asking. A question you could answer by reading is a wasted one.
- **Plain language always.** No jargon in questions; always offer a "not sure" default.
- **Guided confirms; YOLO doesn't. Safety never turns off.** Guardrails, the pipeline-gate, and the safety files ship in every mode. YOLO removes the *chattiness*, not the gate: even in YOLO the flow is definition → approved brief → build, just with less back-and-forth.
- **Ready to use, not a template.** Bake the stack; leave no placeholders; prune dead delegations.
- **Never overwrite living memory on sync.** `PROGRESS/PLAN/DECISIONS` are the user's, not yours.
- **Record the why.** `PROJECT_CONTEXT.md` explains every include and skip.
