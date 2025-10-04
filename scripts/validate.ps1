$ErrorActionPreference = "Stop"

if (-not (Get-Command uv -ErrorAction SilentlyContinue)) {
    Write-Error "'uv' is not installed."
}

Write-Host "=> Running tests"
uv run pytest -q
