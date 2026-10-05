# Project instructions

<!-- instructions-owner: course-maintainers -->
<!-- last-reviewed: 2026-10-05 -->

## Environment

- Use Python 3 and the standard library only.
- Do not install packages or introduce third-party dependencies.
- Source code lives in `src/`; tests live in `tests/`.

## Working boundaries

- Keep public interfaces backward compatible unless the current task explicitly approves a change.
- Do not delete files, disable tests, or broaden the task to unrelated refactoring.
- Ask before installing software, changing a public interface, deleting files, or expanding beyond the requested behavior.

## Default verification

For behavior changes:

1. Read the task source, relevant tests, and implementation.
2. Run `python3 -m unittest discover -s tests -v` before editing and record the baseline.
3. Make the smallest change that satisfies the task.
4. Run the same command after editing.
5. Inspect the diff and report what remains unverified.

## Maintenance

- Keep this file limited to stable project-wide instructions.
- Put task-specific facts in the task source, not here.
- After changing this file or a nested `AGENTS.md`, run the cases in `instruction-evals.md` and review the instruction diff.
- Remove stale, duplicated, or superseded rules instead of only appending new ones.
