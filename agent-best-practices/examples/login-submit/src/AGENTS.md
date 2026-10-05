# Source-specific instructions

- Keep `SubmissionGuard` deterministic and in memory.
- Do not add network, filesystem, database, or process-global state without explicit task approval.
- Preserve the behavior for empty request IDs unless the current task explicitly changes it.
