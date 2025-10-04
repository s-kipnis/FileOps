#!/usr/bin/env bash
set -euo pipefail

# Run tests with pytest via uv.
if ! command -v uv >/dev/null 2>&1; then
  echo "ERROR: 'uv' is not installed."
  exit 1
fi

echo "=> Running tests"
uv run pytest -q
