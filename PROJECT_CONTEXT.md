# Sortex Project Context

## Goal
Build a demonstrable software-and-electronics prototype for an optical sorting machine. The initial software must process video, detect proxy objects, decide accept/reject, map object position to a virtual conveyor/nozzle system, schedule ejection events, and log decisions.

## v0.1 Scope
- Recorded video input only; live camera support is optional.
- Proxy or synthetic dataset allowed.
- Rule-based detection/classification is acceptable.
- Conveyor and pneumatic system may be simulated.
- ESP32 firmware may drive LEDs rather than real 24V valves.
- A 4-channel 24 V MOSFET valve-driver schematic/PCB draft is required.

## Out of Scope for v0.1
- Industrial performance claims.
- Real pneumatic separation accuracy.
- Production deployment.
- Final almond-specific model validation.

## Engineering principles
1. Safety defaults to valves OFF.
2. Do not hard-code machine parameters; use config.
3. Keep vision, control, firmware, hardware, simulation, and logging isolated.
4. Every safety-critical control function needs tests.
5. No agent may modify unrelated files.
6. Every task must state: changed files, tests run, limitations, and next integration point.

## Initial machine assumptions
- Belt width: 300 mm
- Nozzle count: 12
- Camera-to-nozzle distance: 450 mm
- Nominal belt speed: 500 mm/s
- All values are provisional and must live in config files.
