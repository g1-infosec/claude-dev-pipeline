# pipeline-gate

The enforcement layer. Always on. Stops the team collapsing back into one context that does every job.

- **One rule:** no code or product files are written without an approved Implementation Brief in `.claude/memory/BRIEF.md`.
- If a build agent is invoked directly ("PM, build X", "developer, add Y") with no approved brief, it **hard-stops** and routes back to `product-manager` or `project-lead`.
- Narrow, explicit escape hatch only ("skip the pipeline, I take responsibility"); a vague "just build it" does not count.

Details in [`SKILL.md`](./SKILL.md).
