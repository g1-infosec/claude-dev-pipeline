---
name: data-ingestion
description: Activates when working on feed importers, external data pipelines, or any code that pulls data from a third-party source into your datastore.
allowed-tools: [Read, Grep, Glob, Bash]
---

# Data Ingestion Skill

<!-- Adapt: name your feed sources and the paths where ingestion code lives. -->

## Key rules

- **Idempotent.** Re-running an import must never create duplicates. Pick a stable unique key from the source and **upsert**, never blind-insert.
- **Feeds are untrusted.** Validate structure and format before storing; reject malformed records with a warning rather than storing junk.
- **Type discipline.** Store numbers as numbers, booleans as booleans, timestamps as UTC. Never store a number as a string because that's how the feed sent it.
- **No silent gaps.** Log missing date ranges or skipped records explicitly; don't quietly drop data.

## Pipeline order

1. Fetch the feed data.
2. Validate format and completeness.
3. Parse records into your internal schema.
4. Upsert into the datastore (stable unique key).
5. Trigger any downstream processing for new/updated records.

## Error handling

- Retry download failures with exponential backoff (cap the attempts).
- On a partial failure, log the failed record IDs and **continue**; never abort the whole run for one bad record.
- Record the last successful sync timestamp per source.

## Performance

- Process in batches, not one record at a time.
- Use non-blocking I/O throughout the pipeline.
- Cache the raw download locally so you can re-process without re-fetching.
