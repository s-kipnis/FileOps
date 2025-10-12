#!/usr/bin/env pwsh
$ErrorActionPreference = "Stop"
.\.venv\Scripts\Activate.ps1
uvicorn file_ops.app:app --host 127.0.0.1 --port 8000
