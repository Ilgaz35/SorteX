# ESP32 Valve Controller

Target responsibilities:
- Receive `FIRE,<nozzle>,<pulse_ms>`.
- Enforce maximum pulse width.
- Default all outputs to OFF.
- Later: read encoder pulses and publish belt speed.

Implementation begins in `ai_tasks/ehm/TASK-007_firmware_bootstrap.md`.
