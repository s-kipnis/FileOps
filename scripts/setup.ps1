#!/usr/bin/env pwsh
$ErrorActionPreference = "Stop"

if (-not (Get-Command uv -ErrorAction SilentlyContinue)) {
  Write-Error "uv not found. Install: https://docs.astral.sh/uv/"
}

uv venv .venv
uv pip install -U pip
uv pip install -e .
uv pip install -r requirements.txt

Write-Host "✅ Done. Activate: .\.venv\Scripts\Activate.ps1"
