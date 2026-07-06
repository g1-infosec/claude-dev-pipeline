---
name: new-endpoint
description: Activates when adding a new API route or page route, or modifying an existing one.
allowed-tools: [Read, Grep, Glob, Write]
---

# New Endpoint Skill

<!-- Adapt: name your router locations and auth/validation helpers. -->

## Checklist — adding an endpoint

1. **Create or update the router** in the right place (a distinct feature area gets its own file). Register it with the correct prefix.

2. **Input validation.**
   - Every request body goes through a typed, validated model. No raw dicts in handlers.
   - Path and query parameters have explicit types and constraints.
   - Never read the raw request body directly; use the typed model.

3. **Authentication.**
   - Protected endpoints use the shared auth dependency; never inline auth logic in a handler.
   - Enforce **ownership**: an authenticated user may only act on resources they own. Check it explicitly.

4. **Rate limiting.**
   - Every public-facing endpoint is rate-limited.
   - Internal endpoints require a key rather than being open.

5. **Response models.**
   - Return an explicit, typed response model. Never return raw datastore objects.
   - Use one consistent error-response format across all endpoints.

6. **Tests.** Cover the happy path, an auth failure, and invalid input.
