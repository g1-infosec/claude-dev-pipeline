# Changelog

All notable changes to this project are documented here.

## [0.3.0] — 2026-07-05

### Added
- **`pipeline-gate` skill (always-on).** Enforces the team's flow: no code or product files are written without an approved Implementation Brief in `.claude/memory/BRIEF.md`. If a build agent is invoked directly ("PM, build X", "developer, add Y") with no approved brief, it hard-stops and routes back to `product-manager` or `project-lead`.
- **`BRIEF.md`** added to living memory, with a `Status:` line (`NONE` → `DRAFT` → `APPROVED`). `project-lead` writes it; the user approves it; the build agents check it.
- **`/project-setup` slash command** (`.claude/commands/project-setup.md`) so the installer actually runs on a fresh clone. A skill name isn't a slash command on its own; this makes the advertised `/project-setup` real. Plain-language activation still works too.
- **Discovery mode** in `project-setup`: setup now starts from your idea and, when the shape is genuinely open, installs the team with the stack deferred and hands off to the product-manager. The shape and stack get decided in the project-lead's brief and locked in on approval (Finalise).

### Changed
- **Setup is idea-first.** `project-setup` no longer opens by making you pick an architecture (web app / API / CLI) before the product-manager has shaped anything. It asks what you want to build, infers the shape when it's clear, and defers it to the team when it isn't. Deciding the architecture is the team's job, not the price of entry.
- **`product-manager`** now has an explicit hard rule: it never writes code or product files, even when told to "build". It produces a Product Definition and hands off. It also treats an undecided product *shape* as normal, flagging it for the project-lead rather than assuming one.
- **`project-lead`** now writes its brief to `BRIEF.md`, marks it `APPROVED` only on the user's "go", and (in discovery mode) must recommend the shape and stack in the brief.
- **Build agents** (`developer`, `ui-ux`, `db-engineer`, `devops`) now open with a gate precondition: read `BRIEF.md`, refuse to build if it isn't `APPROVED`, and route back.
- **`ui-ux`** degrades gracefully when no browser/Playwright tool is present: it skips the screenshot step and verifies by other means instead of blocking.
- Setup includes `pipeline-gate` in every archetype and seeds `BRIEF.md`. The gate stays on in YOLO mode; YOLO reduces chatter, not the gate.

### Fixed
- **Repo layout, take two: edit in place.** The library of role and skill templates now lives in `template/`, and setup writes your tailored team into the same repo's `.claude/` — the clone *is* your project. `project-setup` stays in `.claude/skills/` so `/project-setup` still loads on a clone. Setup gitignores `template/` so the library doesn't ride along in your project history. Earlier this release the agents/skills briefly moved under `.claude/`; the in-place `template/` split supersedes that.
- **Monorepo self-target false positive.** `project-setup` no longer aborts on a monorepo just because an `.aidevteam` marker is found up the tree. With edit-in-place the default target is simply the current repo; you only name a path for a specific monorepo package.

### Why
- Fixes the failure where a direct "product-manager, build X" collapsed the whole team back into one context that shrugged on the PM hat for a sentence and started writing files. The pipeline was documented but not defended; now it is.

## [0.2.0] — 2026-07-05

### Added
- **Archetypes** in `project-setup`: pick "what are you building?" (web app, static site, API, CLI, bot, extension, mobile, data/ML) and the team pre-wires itself. Handles greenfield/empty repos.
- **Guided vs YOLO modes.** Guided confirms and gates; YOLO just builds. Safety checks stay on in both.
- **Living project memory** (`project-memory` skill): `PLAN.md`, `DECISIONS.md`, `PROGRESS.md` under `.claude/memory/`, read at the start and updated at the end of every agent's work. The team stops forgetting between sessions.
- **`debugger`** agent: diagnoses "it's broken, why?" before anyone edits.
- **`docs-writer`** agent: keeps the README honest and current.
- **`smoke-test`** skill: "it builds, it boots, the homepage loads" before anything is called done.
- **`guardrails`** skill: secrets, `.gitignore`, branch-not-main, back-up-before-migrate.
- Setup now seeds `.gitignore` and `.env.example`, and prunes delegations to skipped roles.
- **Sync** path to pull upstream agent improvements into an existing `.claude/` without touching living memory.
- Repo furniture: `LICENSE`, `CONTRIBUTING`, issue/PR templates.

## [0.1.0] — initial

- Eight-role agnostic dev team (product-manager, project-lead, developer, ui-ux, db-engineer, devops, qa-engineer, security-auditor) with a delivery pipeline.
- Skills: security-review, new-endpoint, db-migration, data-ingestion, new-agent.
- `project-setup` skill: interview, infer roster, write tailored copies into `.claude/`.
