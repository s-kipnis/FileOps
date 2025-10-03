#!/usr/bin/env pwsh
$ErrorActionPreference = "Stop"
. .\.venv\Scripts\Activate.ps1
pytest -q
