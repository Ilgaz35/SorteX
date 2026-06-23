# Development Setup

## Windows PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pytest
ruff check .
```

Use one focused task at a time from `ai_tasks/ehm/`.
