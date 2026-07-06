# project-setup

The installer. Run this from inside the cloned repo to stand up a tailored team in another project.

- **Run it:** `/project-setup` (or "set up the dev team for &lt;path&gt;")
- **What it does:** picks an archetype, asks a few plain-language questions, infers the roster and stack, and writes ready-to-use agents, skills, and living-memory files into the target project's `.claude/`.
- **Modes:** guided (confirms + gates) or YOLO (just builds). Safety stays on in both.
- **Sync:** re-run and say "sync" to pull upstream agent updates without touching your memory.

Full behaviour in [`SKILL.md`](./SKILL.md).
