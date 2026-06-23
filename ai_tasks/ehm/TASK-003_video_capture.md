# TASK-003 — Video Capture Module

## Goal
Implement a testable recorded-video input module.

## Allowed paths
- `src/sortex/vision/camera_capture.py`
- `src/sortex/vision/__init__.py`
- `tests/test_camera_capture.py`
- `scripts/`
- `docs/`

## Acceptance criteria
- Opens an MP4/video path safely.
- Produces frame ID, timestamp in milliseconds, frame image, fps, width, and height.
- Releases resources reliably.
- Fails with a clear exception for an invalid path.
- Includes a test strategy that does not require a large committed video file.

## Integration
The output must be easy for `object_detection.py` to consume.
