# TASK-007 — ESP32 Firmware Bootstrap

## Goal
Create a safe ESP32 firmware skeleton for future valve commands.

## Allowed paths
- `firmware/esp32_valve_controller/`
- `docs/communication_protocol.md`
- `docs/pin_mapping.md`
- `tests/` (host-side protocol tests only)

## Acceptance criteria
- Uses PlatformIO structure.
- Defines a `FIRE,<nozzle>,<pulse_ms>` parser specification.
- Defines `STOP_ALL`, `PING`, and `HEARTBEAT` behavior.
- All output pins default LOW/OFF.
- Defines a configurable max pulse width.
- Does not assume the final valve-driver PCB is built.
