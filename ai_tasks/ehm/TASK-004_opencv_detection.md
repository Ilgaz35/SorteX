# TASK-004 — Basic OpenCV Detection

## Goal
Create a configurable proxy-object detection module using OpenCV.

## Allowed paths
- `src/sortex/vision/`
- `config/`
- `tests/`
- `docs/`

## Acceptance criteria
- Uses configurable preprocessing thresholds.
- Detects contours and filters noise by area.
- Returns typed `DetectionEvent` candidates or an intermediate typed detection structure.
- Does not classify the object beyond a safe placeholder decision.
- Includes synthetic-image unit tests.

## Out of scope
YOLO training, final almond classes, and video UI.
