---
name: smoke-test
description: 'Activates after a build step, before declaring anything done, and whenever the user asks "does it work / does it run / did I break it". A fast, shallow check that the thing actually starts and the main paths respond, not deep behaviour tests. This is the gate vibecoders care about most: "it builds, it boots, the homepage loads." '
allowed-tools: [Read, Bash, Glob, Grep]
---

# Smoke Test

Before you tell the user something works, confirm it actually runs. This is not the full test suite (that's `qa-engineer`). It's the shallow, fast "is it alive" check that catches the embarrassing breakages: it doesn't compile, the server won't boot, the page 500s on load.

## The checklist (run what applies)

1. **It builds / compiles.** Run the build or type-check. No errors.
2. **It starts.** Boot the app/server/process. It comes up without crashing.
3. **The main path responds.** Hit the primary entry point:
   - Web app: load the homepage and one key page; expect a 200, not a 500 or a blank screen.
   - API/service: call the health endpoint and one real endpoint; expect a valid response.
   - CLI: run `--help` and one real command; expect sane output, exit code 0.
4. **Nothing obvious is on fire.** Check the logs on startup for errors or missing-env-var warnings.

## Output format

---
### 🚦 Smoke Test: [what was checked]

- Build/compile: ✅ / ❌ [detail if failed]
- Starts up: ✅ / ❌ [detail]
- Main path responds: ✅ / ❌ [what was hit, what came back]
- Startup logs clean: ✅ / ⚠️ [any warnings]

**Verdict:** RUNS ✅ / BROKEN ❌

**If BROKEN:** [the exact error, and hand it to `debugger`]
---

## Rules

- **Shallow and fast.** Seconds to a couple of minutes. If you're writing detailed assertions, that's `qa-engineer`'s job, not this.
- **Actually run it.** Don't infer "it should work." Boot it and hit it.
- **A broken smoke test blocks "done."** Never report a feature complete if it doesn't start or the main page errors. Hand the failure to `debugger`.
- **Report env problems clearly.** Missing environment variables are the #1 vibecoder startup failure; call them out by name and point at `.env.example`.
