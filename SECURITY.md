# Security Policy

## Reporting a vulnerability

Please do not open a public issue for security problems.

The preferred channel is GitHub's private vulnerability reporting: go to the
**Security** tab of this repository and choose **Report a vulnerability**. If you
cannot use that, email **security@g1-infosec.example** (replace with the real
address before publishing) with enough detail to reproduce.

You can expect an acknowledgement within 3 working days and a fuller response,
including next steps, within 10 working days. Please give us a reasonable window
to remediate before any public disclosure.

## Scope

This is a template repository. The security surface that matters here is the
tooling this repo ships, not the applications people build with it. In scope:

- The `project-setup` skill and slash command (for example, unsafe file
  operations, path traversal, or command injection when resolving the repo
  marker or writing into `.claude/`).
- The `guardrails`, `security-review`, and `smoke-test` skills failing in a way
  that removes a protection users rely on (for example, secrets being committed
  without a warning firing).
- Handling of credentials or secrets anywhere in the template or setup flow.

Out of scope:

- Vulnerabilities in projects generated *by* the pipeline. Those belong to the
  downstream project, not this template.
- Behaviour of the underlying model or of Claude Code itself.
- Findings that require the user to deliberately disable the safety checks
  (for example, an explicit pipeline override).

## Supported versions

The latest tagged release and `main` receive fixes. Older tags do not.
