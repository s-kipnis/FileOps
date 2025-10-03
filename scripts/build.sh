#!/usr/bin/env bash
set -euo pipefail
# Сборка wheel через uv/hatchling
uv build
ls -1 dist/
