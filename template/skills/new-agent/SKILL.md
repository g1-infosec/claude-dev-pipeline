---
name: new-agent
description: Activates when adding a new stage agent to a multi-agent processing pipeline, or modifying the orchestrator/coordinator that runs it.
allowed-tools: [Read, Grep, Glob, Write]
---

# Add a Pipeline Agent — Skill

<!-- Adapt: name your agents / schemas / prompts / coordinator locations. -->

## Checklist

1. **Agent file** — one async entry point: `run_my_agent(input, client) -> MyAgentOutput`.
   - Use the **shared** model client; never instantiate a new one inside an agent.
   - Wrap the call in the cache layer: check cache before calling, store after.

2. **Output schema** — a typed, validated model (not a raw dict).
   - Every field has a description; downstream code and any UI depend on them.
   - Include a `prompt_version` string.

3. **Prompt template** — include the explicit constraints: "Base your response only on the provided input" and "Do not speculate beyond what the input supports." Put a version string at the top that matches the schema's `prompt_version`.

4. **Register in the coordinator** — add the call to the correct concurrency phase (independent work in phase 1; work that depends on phase 1 in phase 2). Wrap it in the fallback wrapper, add its output to the merge logic, and add its usage to cost tracking.

5. **Test** — fixture inputs; cover the normal case, empty input, and malformed input; assert the output validates against the schema.

## Prompt-version rule

Bump the version string every time you change a prompt. The cache key includes it, so bumping it invalidates just that stage's cache and forces a re-run on next request.

## Anti-patterns

- Never have one agent call another directly; all orchestration goes through the coordinator.
- Never hardcode specific record data or IDs in a prompt.
- Never return a free-form string from an agent; always a validated schema object.
