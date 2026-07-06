---
name: security-review
description: Activates when reviewing or modifying auth code, token handling, API endpoints, user-input processing, middleware, or any logic that gates access to resources. Also activates when adding or modifying routes.
allowed-tools: [Read, Grep, Glob]
---

# Security Review Skill

When activated, always check the following before completing the task.

## Authentication & tokens
- Every protected route validates the auth token via the shared middleware.
- Token expiry is enforced; never accept a token without an expiry claim.
- Never log tokens or secrets in any form.

## Input validation
- All external input goes through a typed, validated model. No raw dicts in handlers.
- Validate structured inputs (IDs, codes, formats) against their known shape before processing.
- Never pass raw user input into a query, command, or file path. Use parameterised queries.

## API security
- Every public-facing endpoint is rate-limited.
- Access-controlled resources verify **ownership**: the authenticated user owns the thing they're acting on.
- Internal endpoints require a key; they are never reachable open.

## External model / LLM calls (if any)
- Prompts derive only from verified, stored data; never pass unverified third-party data into a prompt.
- Prompts include explicit instructions against speculation, and output is validated before use.

## Secrets & configuration
- No secrets, keys, or credentials in source. Environment variables only.
- Never write to secret/config files programmatically.
- Verify config loads sensitive values from the environment, not hardcoded defaults.

## Report format
List findings as:
- **[CRITICAL / HIGH / MEDIUM / LOW]** `file:line` — description and recommended fix.
