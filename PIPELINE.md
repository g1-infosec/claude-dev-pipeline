# The Delivery Pipeline

How an idea becomes shipped work. Two approval gates keep you in control; everything between them runs on scoped context.

> **Wrapping every step:** the `project-memory` skill. Each agent reads `.claude/memory/` (PLAN, DECISIONS, PROGRESS, BRIEF) before it starts and updates it after, so the team stays continuous across sessions. **Enforced at every step:** the `pipeline-gate` skill. No build agent writes code without an `APPROVED` brief in `.claude/memory/BRIEF.md`; a direct "just build it" gets routed back to the product-manager or project-lead, not actioned. **On the side, always available:** the `debugger` agent for "it's broken, why?", and the `guardrails` skill for secrets and destructive-action safety.

## The flow

```
   YOU
    │  "here's my idea"
    ▼
┌─────────────────────┐
│  product-manager    │  shapes idea → PRODUCT DEFINITION
│  (no code)          │  problem · audience · user stories · acceptance · out-of-scope
└─────────┬───────────┘
          │  ── approval gate 1 (you approve the definition) ──
          ▼
┌─────────────────────┐
│   project-lead      │  reads the code → IMPLEMENTATION BRIEF
│   (no code)         │  task table → specialists · risks · execution order
└─────────┬───────────┘
          │  ── approval gate 2 (you approve the plan) ──
          ▼
      BUILD  (dependency order, each scoped)
   ┌──────────────┬──────────────┬──────────────┬──────────────┐
   ▼              ▼              ▼              ▼
db-engineer  →  developer   →   ui-ux          devops (prep)
   │              │              │
   └──────────────┴──────────────┘
                  │
                  ▼
      REVIEW GATES  (before ship)
   ┌──────────────┬──────────────┬──────────────┬──────────────┐
   ▼              ▼              ▼              ▼
security-      qa-            smoke-test     product-
auditor        engineer       (runs/boots?)  manager
PASS/BLOCK     tests          RUNS/BROKEN    SHIP/NEEDS WORK
   └──────────────┴──────────────┴──────────────┘
                  │  (all green)
                  ▼
            docs-writer  (refresh the README)
                  │
                  ▼
              devops
              ship + rollback + runbook
                  │
                  ▼
                SHIPPED  → update .claude/memory/PROGRESS.md
```

`[optional: redraw as a clean left-to-right diagram for a README hero or slide]`

## The two documents that carry the work

### Product Definition (from product-manager)
The idea, made concrete enough to build. Sections: **Problem statement**, **User stories** (per audience), **Acceptance criteria**, **Out of scope**, **Open questions**, **Biggest risk**. You approve it at gate 1. If you can't say what "done and good" looks like from it, it isn't finished.

### Implementation Brief (from project-lead)
The plan, mapped to the team. Sections: **What we're building**, **Scope / does-not-touch**, **Risks & flags**, **Work plan** (task → specialist table), **Execution order** (with dependencies), **How to invoke**. You approve it at gate 2.

## Execution order (the default dependency chain)

1. **db-engineer** — schema and migrations land first; everything else builds on the data shape.
2. **developer** — logic, APIs, integrations against that schema.
3. **ui-ux** — the interface against real endpoints.
4. **devops** — packaging, config, deploy prep, in parallel where it can be.

Then the gates:

5. **security-auditor** — read-only, adversarial. A `BLOCK` stops the ship until fixed and re-reviewed.
6. **qa-engineer** — tests behaviour, not implementation. Writes tests; never edits app code.
7. **product-manager** — the user's advocate. Does this actually solve the problem in the definition? `SHIP IT`, `NEEDS WORK`, or `RETHINK`.

## Why the gates matter

The product-manager and project-lead never write code, and the reviewers never write features. That separation is the point: the planner keeps the big picture so the builders don't have to, and the reviewers stay adversarial because they have no authorship to defend. You approve twice (the what, then the how) and stay out of the middle.

## Scaling down

Not every idea needs the full chain. The project-lead will tell you when a step is overkill (a copy change doesn't need a db-engineer). For genuinely small work, skip the team and use a single prompt. The tell that you need the team: the work touches more than one part of the system, or you're re-pasting context to keep the model on track.
