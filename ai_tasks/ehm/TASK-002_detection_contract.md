# TASK-002 — Detection Event Contract

## Goal
Finalize the typed cross-module contract used between vision and control.

## Allowed paths
- `src/sortex/models/`
- `tests/test_detection_event.py`
- `ARCHITECTURE.md`
- `docs/`

## Acceptance criteria
- `DetectionEvent` validates sensible numeric ranges where practical.
- Add an `EjectionEvent` dataclass without importing OpenCV.
- Add tests for valid and invalid construction.
- Keep contracts serializable or easily convertible to dict/JSON.

## Do not
Do not implement actual object detection or scheduler logic.
