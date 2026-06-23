# Architecture

## Data flow

```text
VideoFrame
  -> DetectionEvent
  -> ClassificationDecision
  -> PositionedObject
  -> EjectionEvent
  -> ValveCommand
  -> LogRecord
```

## Module boundaries

- `src/sortex/vision/`: frame capture, preprocessing, detection, visualization.
- `src/sortex/models/`: typed events shared across modules.
- `src/sortex/control/`: coordinate mapping, conveyor model, nozzle mapping, scheduler, event queue.
- `src/sortex/simulation/`: virtual conveyor, virtual nozzle board, mock hardware.
- `src/sortex/hardware/`: serial interface and protocol models.
- `src/sortex/data/`: logging and metrics.
- `firmware/`: ESP32 code; must not depend on Python code.

## Integration contract: DetectionEvent

```json
{
  "object_id": 42,
  "frame_id": 186,
  "timestamp_ms": 125000,
  "class_name": "shell_fragment",
  "decision": "reject",
  "confidence": 0.91,
  "center_px": [960, 420],
  "bbox_px": [910, 380, 100, 80]
}
```

## Integration contract: EjectionEvent

```json
{
  "object_id": 42,
  "target_nozzle": 5,
  "scheduled_fire_timestamp_ms": 125820,
  "pulse_width_ms": 30,
  "status": "scheduled"
}
```

## Firmware command

```text
FIRE,5,30
```
