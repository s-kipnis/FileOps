#!/usr/bin/env bash
set -euo pipefail

# Ensure uv is available
if ! command -v uv >/dev/null 2>&1; then
  echo "uv not found. Install: https://docs.astral.sh/uv/"
  exit 1
fi

# Create venv and install deps (editable install)
uv venv .venv
uv pip install -U pip
uv pip install -e .
# Tooling + test runner
uv pip install -r requirements.txt

echo "✅ Done. Activate: source .venv/bin/activate"
