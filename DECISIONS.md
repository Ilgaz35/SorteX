# Architecture Decision Log

## ADR-001: v0.1 uses proxy/synthetic data
Reason: Real almond data is not yet available. The first release validates pipeline integration, not industrial model accuracy.

## ADR-002: bbox detection before segmentation
Reason: Nozzle mapping needs object center coordinates; bounding boxes are enough for the first scheduling prototype.

## ADR-003: hardware is abstracted
Reason: The Python control plane must run with a mock controller before physical board integration.

## ADR-004: safety defaults to OFF
Reason: A late event or communication loss must not leave a valve energized.
