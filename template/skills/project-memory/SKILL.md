---
name: project-memory
description: The team's shared, living memory. Activates at the start and end of ANY agent's work in a project that has a .claude/memory/ folder. Every agent reads PLAN.md, DECISIONS.md, and PROGRESS.md before acting, and updates them after. This is what keeps the team continuous across sessions instead of forgetting what was decided and what's half-built.
allowed-tools: [Read, Write, Glob, Grep]
---

# Project Memory

This is the single most important habit in the team. Models forget between sessions; this convention is how the team remembers. Three small files under `.claude/memory/` carry the project's continuity. **Every agent reads them before starting and updates them before finishing.**

## The three files

### `PLAN.md` — what we're doing and what's next
A living checklist, newest state at the top. Not a spec; a to-do that survives the session.
```
# Plan

## Now
- [ ] <the one thing being worked on>

## Next
- [ ] <upcoming task>  (owner: developer)
- [ ] <upcoming task>  (owner: ui-ux)

## Done
- [x] <completed task>  (2026-07-05)
```

### `DECISIONS.md` — why we chose what we chose
An append-only log so nobody re-litigates settled questions. One entry per decision.
```
# Decisions

## 2026-07-05 — Auth approach
Chose session cookies over JWT. Reason: single web app, no third-party API consumers yet.
Revisit if: we add a public API or a mobile client.
```

### `PROGRESS.md` — the state of the build, in plain language
A short status a non-technical person could read. What works, what's half-built, what's broken.
```
# Progress

**Working:** signup, login, the dashboard shell.
**Half-built:** the settings page (UI done, not wired to the backend).
**Broken / known issues:** password reset email doesn't send yet.
**Last session ended:** mid-way through the settings backend.
```

### `BRIEF.md` — the approved build plan (the gate)
Written by `project-lead`, approved by the user. Carries a `Status:` line (`NONE` → `DRAFT` → `APPROVED`). The `pipeline-gate` skill checks this before any build agent writes code: no `Status: APPROVED`, no building. Read it to know what the team is currently authorised to build.

## The loop (every agent, every time)

**At the start of your work:**
1. Read `PLAN.md`, `DECISIONS.md`, and `PROGRESS.md`. This is your memory of the project.
2. Respect existing decisions. If you think one is wrong, raise it; don't silently reverse it.

**At the end of your work:**
1. Tick off what you finished in `PLAN.md`; add any new tasks you discovered.
2. If you made a real choice (a tradeoff, a library, an approach), append it to `DECISIONS.md` with a one-line reason.
3. Update `PROGRESS.md` so the next session (or the next agent) knows exactly where things stand.

Keep updates short. This is a memory, not a diary. A vibecoder should be able to open `PROGRESS.md` after a week away and know exactly where they left off.

## Rules

- **Read before you build. Update before you stop.** Non-negotiable. A session that ends without updating memory is a session half-lost.
- **DECISIONS.md is append-only.** Never edit or delete a past decision; add a new one that supersedes it and say so.
- **Plain language in PROGRESS.md.** The person who owns this project may not read code. They can read this.
- **If the files don't exist yet**, create them (project-setup normally seeds them). Don't proceed without them.
