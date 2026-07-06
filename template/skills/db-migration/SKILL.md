---
name: db-migration
description: Activates when modifying data models, creating migrations, or making any database schema change.
allowed-tools: [Read, Grep, Glob, Bash, Write]
---

# DB Migration Skill

<!-- Adapt: name your ORM, migration tool, and model file locations. -->

## Checklist — schema changes

1. **Update the model.**
   - New columns on an existing, populated table must be nullable or have a default. Never add a NOT NULL column without a default to a table that already has rows: it will fail.
   - Add indexes for columns used in filters or joins.

2. **Generate the migration** with your tool. Then **review the generated file by hand** before running it. Auto-generation is not always right.
   - Confirm both the up and the down are correct.
   - Never commit a migration with an empty down/rollback.

3. **Run it**, then **verify** you're at the expected head.

## Rules

- **Always test the rollback:** migrate down one, then back up, before you call it done.
- **Never edit a migration that's already been applied to production.** Create a new one.
- **Data migrations** (not just schema) should use explicit statements in the migration, not your application's ORM, which may have moved on by the time the migration re-runs.

## Common footguns

- Adding a non-nullable column to a populated table without a default: fails.
- Renaming a column: most auto-generators emit a drop + add (which loses data) instead of a rename. Write the rename explicitly.
