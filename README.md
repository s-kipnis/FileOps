# FileOps

Minimal: Starlette + Uvicorn, to wheel, tools: uv, ruff, mypy, pylint.

## Quick Start

```bash
# Bash
./scripts/setup.sh
./scripts/run.sh
```

```PowerShell
.\scripts\setup.ps1
.\scripts\run.ps1
```

# Endpoints
- GET /health → {"status":"ok"}
- POST /send → эхо-сообщение (JSON или text/plain)

Lint
```bash 
./scripts/lint.sh
# or
.\scripts\lint.ps1
```

Test
`./scripts/test.sh`

Build:
```
./scripts/build.sh
# или
.\scripts\build.ps1
```
