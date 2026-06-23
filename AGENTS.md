# Sortex Agent Instructions

Read `PROJECT_CONTEXT.md`, `ARCHITECTURE.md`, `DECISIONS.md`, and the selected file under `ai_tasks/` before changing code.

## Required workflow
1. State a concise implementation plan.
2. Touch only the files allowed by the task.
3. Preserve module boundaries.
4. Add or update tests for logic changes.
5. Run relevant tests and linting.
6. Report changed files, test commands/results, assumptions, limitations, and a suggested commit message.

## Python rules
- Python 3.11+.
- Type hints on public functions and dataclasses for cross-module events.
- Use pathlib; avoid hard-coded local paths.
- Keep business logic independent of OpenCV and serial hardware.
- Machine parameters must come from config.
- No hidden global state.

## Safety rules
- All valve outputs must default to OFF.
- A late or invalid ejection event must be logged and not fired blindly.
- Every pulse must have an upper bound.
- Hardware interfaces require a mock implementation.

## Prohibited actions
- Do not delete unrelated files.
- Do not replace the repository architecture without an explicit task.
- Do not claim performance that has not been measured.
- Do not commit raw datasets, videos, virtual environments, or secrets.
