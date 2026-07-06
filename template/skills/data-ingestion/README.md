# data-ingestion

Idempotent, resilient import of data from external feeds and APIs.

- **Included when:** the project pulls in data from third-party sources.
- Upsert not blind-insert; validate before store; treat every feed as untrusted; never abort a whole run for one bad record.

Details in [`SKILL.md`](./SKILL.md).
