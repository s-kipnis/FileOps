#!/usr/bin/env pwsh
$ErrorActionPreference = "Stop"
uv build
Get-ChildItem dist
