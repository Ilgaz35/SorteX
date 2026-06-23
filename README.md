<<<<<<< HEAD
# SorteX
Computer Vision and automation project for industry
||||||| (empty tree)
=======
# Sortex Vision & Ejection Control Prototype

A modular proof-of-concept for an AI-assisted optical sorting system. Version `v0.1.0` validates the digital chain:

`video input -> object detection -> accept/reject decision -> pixel-to-mm mapping -> nozzle assignment -> ejection scheduling -> virtual/embedded valve command -> logging`

## Status

Early engineering prototype. The first dataset may be proxy/synthetic; it is not a claim of industrial almond-sorting performance.

## Quick start

```bash
python -m venv .venv
# Windows PowerShell:
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pytest
python scripts/run_video_demo.py
```

## Core documents

- `PROJECT_CONTEXT.md`: Product and MVP constraints.
- `ARCHITECTURE.md`: Module boundaries and data contracts.
- `AGENTS.md`: Persistent instructions for coding agents.
- `ai_tasks/ehm/`: EHM-owned task packages.
>>>>>>> 8a2f1ef (chore: initialize sortex prototype architecture)
