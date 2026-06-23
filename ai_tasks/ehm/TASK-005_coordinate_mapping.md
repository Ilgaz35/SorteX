# TASK-005 — Pixel-to-mm Mapping

## Goal
Map image X coordinates to physical belt X coordinates for nozzle assignment.

## Allowed paths
- `src/sortex/control/coordinate_mapper.py`
- `config/default_machine_config.yaml`
- `tests/test_coordinate_mapper.py`
- `docs/calibration.md`

## Acceptance criteria
- Supports a simple linear mapping based on image width and belt width.
- Handles left edge, center, right edge, and invalid X values.
- Uses config, never hard-coded dimensions.
- Documents why this is an MVP approximation and when homography/lens calibration is needed.
