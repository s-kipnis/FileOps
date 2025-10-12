#!/usr/bin/env bash
set -euo pipefail
source .venv/bin/activate
uvicorn file_ops.app:app --host 127.0.0.1 --port 8000
