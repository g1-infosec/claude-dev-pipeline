# smoke-test

The "does it actually run?" gate. Always on, before anything is called done.

- Shallow and fast: it builds, it boots, the main page/endpoint responds, the logs are clean.
- Not the full test suite (that's `qa-engineer`); this catches the embarrassing breakages.
- A broken smoke test blocks "done" and hands the failure to `debugger`.

Details in [`SKILL.md`](./SKILL.md).
