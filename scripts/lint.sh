#!/usr/bin/env bash
set -euo pipefail
source .venv/bin/activate

echo "Ruff (lint + import sort + format) ..."
ruff check --fix .
ruff format .

echo "mypy ..."
mypy .

echo "pylint ..."
pylint src/file_ops
