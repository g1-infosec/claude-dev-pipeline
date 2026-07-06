---
name: pipeline-gate
description: 'Always-on enforcement of the team''s pipeline. Activates whenever any agent is about to write or edit code or project files. It enforces one rule: nothing gets built without an approved Implementation Brief. If a build agent is invoked directly (e.g. "product-manager, build X" or "developer, add Y") and there is no approved brief, it hard-stops and routes back to the right step. This is what stops the team collapsing back into one context doing every job.'
allowed-tools: [Read, Glob, Grep]
---

# Pipeline Gate

The whole point of this team is that work flows **idea → definition → approved brief → build → review**. Left undefended, that flow collapses: someone says "PM, build me X", the agent shrugs on the PM hat for a sentence and starts writing files, and you're back to one overloaded context doing every job. This skill is the defence. It is always on.

## The one rule

**No code or project files are written without an approved Implementation Brief in `.claude/memory/BRIEF.md`.**

"Code or project files" means application source, config, HTML/CSS/JS, schema, infra files, anything that is the product. It does **not** mean the team's own planning files (`BRIEF.md`, `PLAN.md`, `DECISIONS.md`, `PROGRESS.md`, `PROJECT_CONTEXT.md`), which the planning roles write as part of the flow.

## The check (run before writing anything)

Before a build agent (`developer`, `ui-ux`, `db-engineer`, `devops`, or any specialist) writes or edits a product file:

1. **Read `.claude/memory/BRIEF.md`.**
2. It counts as an **approved brief** only if it exists, describes the current task, and is marked approved (a `Status: APPROVED` line, or an explicit user "go" recorded against it).
3. **If there is no approved brief for this task → HARD STOP.** Do not write. Respond with the routing message below.

## Hard stop, and route back

When the gate blocks, say plainly what happened and where to go next. Route to the correct step depending on how far along things are:

- **No definition yet** (a raw idea like "build me X") → route to `product-manager`:
  > I can't start building yet — this team works by shaping the idea first. Let me hand this to the **product-manager** to turn "<the request>" into a short Product Definition. You approve that, then the **project-lead** turns it into a plan, and *then* I build. Want me to start with the product-manager?
- **Definition exists but no approved brief** → route to `project-lead`:
  > There's a product definition but no approved build plan yet. The **project-lead** needs to turn it into an Implementation Brief for you to approve before I write code. Shall I do that?
- **Brief exists but isn't approved** → ask for approval, don't assume it:
  > The brief is ready but not approved. Reply "go" to approve it and I'll start building to it.

Never write the product file "just this once." The exception is the crack the whole thing leaks through.

## Roles this gate binds

- **product-manager** never writes code or product files, even when the user says "build". It produces a Product Definition and stops.
- **project-lead** never writes code. It produces the Implementation Brief and writes it to `BRIEF.md`; the user approves it.
- **build agents** (`developer`, `ui-ux`, `db-engineer`, `devops`) check for the approved brief first and refuse if it's missing.
- **reviewers** (`security-auditor`, `qa-engineer`) don't need a brief to review, but they never write features.

## Emergency escape hatch (deliberately narrow)

If the user *explicitly* overrides with something unambiguous like "skip the pipeline, just write it, I take responsibility", you may proceed, but:
1. Say once that you're bypassing the pipeline at their request.
2. Still run `guardrails` (secrets, branch, backups never turn off).
3. Record the bypass in `DECISIONS.md`.

A vague "just build it" is **not** an override; that's the normal request the gate exists to catch. Only an explicit instruction to skip the process counts.

## Rules

- **Default is stop, not proceed.** When in doubt about whether a brief is approved, treat it as not approved.
- **The gate protects product files only.** Never let it block the planning roles from writing the memory/brief files that move the flow forward.
- **Route, don't just refuse.** Always tell the user the next concrete step and offer to take it.
