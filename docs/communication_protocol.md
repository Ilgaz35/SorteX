# Communication Protocol (Draft)

## Commands
- `FIRE,<nozzle>,<pulse_ms>`: schedule immediate output pulse at MCU level.
- `STOP_ALL`: force every output OFF.
- `PING`: liveness check.
- `HEARTBEAT`: host liveness message.

## Safety
- Invalid commands return `NACK`.
- Pulse width above configured maximum must be rejected.
- Loss of heartbeat must force outputs OFF.
