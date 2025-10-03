#!/usr/bin/env pwsh
$ErrorActionPreference = "Stop"
. .\.venv\Scripts\Activate.ps1

Write-Host "Ruff (lint + import sort + format) ..."
ruff check --fix .
ruff format .

Write-Host "mypy ..."
mypy .

Write-Host "pylint ..."
pylint src/file_ops
