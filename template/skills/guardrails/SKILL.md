---
name: guardrails
description: Always-on safety net against self-inflicted damage. Activates before commits, before migrations, before destructive commands, and whenever secrets or credentials are involved. Catches the dumb, costly mistakes inexperienced builders make: committing secrets, working on main, running a destructive migration with no backup, deleting things they can't get back.
allowed-tools: [Read, Grep, Glob, Bash]
---

# Guardrails

Vibecoders rarely get hurt by subtle bugs; they get hurt by avoidable accidents. This skill is the seatbelt. When any of these situations come up, stop and enforce the check before proceeding.

## Secrets

- **Before any commit**, scan staged changes for secrets: API keys, tokens, passwords, connection strings, private keys, `.env` files. If found, **stop** and tell the user to remove them and add them to `.gitignore`.
- Secrets belong in a `.env` file that is gitignored, with a safe `.env.example` (keys, no values) committed instead.
- Never print a real secret in output or logs.

## Version control

- **Work on a branch, not `main`**, for anything non-trivial. If the user is on `main`, suggest a branch before big changes.
- **Commit before risky work.** A clean checkpoint means mistakes are one `git reset` away from undone. Prompt for a commit before large or destructive operations.
- Ensure a `.gitignore` exists and covers secrets, dependencies, and build output.

## Destructive operations

- **Before any database migration**, especially one that drops or renames, confirm there's a backup or that the data is disposable. Say so explicitly and get a yes.
- **Before deleting files, dropping tables, or force-pushing**, confirm intent and confirm it's recoverable. Name what will be lost.
- Never run a destructive command "to see if it works."

## Dependencies

- Flag installing packages from untrusted or unfamiliar sources.
- Prefer pinned versions over floating ones for anything that ships.

## The pattern

When a guardrail triggers:
1. **Stop** before the risky action.
2. **Name the risk** in one plain sentence.
3. **Offer the safe path** (branch, backup, gitignore, commit).
4. Proceed only once the user confirms or the safe path is in place.

## Rules

- **Loud on secrets and data loss.** These are the two that ruin someone's week. Never let them slide with a soft warning.
- **Safe path, not a lecture.** Give the one action that makes it safe, don't moralise.
- **Recoverable by default.** Before anything irreversible, make sure there's a way back, or make the user say "yes, I know" on purpose.
