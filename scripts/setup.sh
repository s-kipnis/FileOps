#!/usr/bin/env bash
set -euo pipefail

# Setup project using uv; no requirements*.txt are used.
if ! command -v uv >/dev/null 2>&1; then
  echo "ERROR: 'uv' is not installed. See https://docs.astral.sh/uv/"
  exit 1
fi

make setup
