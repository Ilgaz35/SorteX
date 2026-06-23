# TASK-006 — Ejection Scheduler

## Goal
Implement safe scheduling logic from a reject event to a future valve command.

## Allowed paths
- `src/sortex/control/ejection_scheduler.py`
- `src/sortex/models/`
- `config/`
- `tests/test_ejection_scheduler.py`
- `docs/latency_budget.md`

## Acceptance criteria
- Computes travel time from camera-to-nozzle distance and belt speed.
- Subtracts separately configured system delays.
- Rejects or logs late/unsafe events rather than firing blindly.
- Enforces max pulse width.
- Returns a typed `EjectionEvent`.
- At least 8 focused tests cover normal, slow, fast, zero-speed, negative-delay, and invalid-pulse cases.
