# Requires: PowerShell 5+ / 7+, uv installed
$ErrorActionPreference = "Stop"

if (-not (Get-Command uv -ErrorAction SilentlyContinue)) {
    Write-Error "uv is not installed. See https://docs.astral.sh/uv/"
}

Write-Host "=> Syncing environment via uv (pyproject + uv.lock)"
uv sync
Write-Host "=> Done."
