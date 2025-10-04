VENV := .venv
UV := uv
VENV_BIN := $(VENV)/Scripts
VENV_MARKER := $(VENV)/.timestamp

ifeq ($(OS),Windows_NT)
    PYTEST := $(VENV_BIN)/pytest.exe
else
    VENV_BIN := $(VENV)/bin
    PYTEST := $(VENV_BIN)/pytest
endif

.PHONY: setup dev build test clean


$(MARKER): pyproject.toml
	@echo "⚠️  Rebuilding venv because pyproject.toml changed"
	@rm -rf $(VENV)
	@uv venv $(VENV)
	@uv sync --locked --all-extras
	@touch $(MARKER)

setup: $(MARKER)
	@echo ".venv is up to date."

build: setup
	$(UV) sync --locked --no-dev
	$(UV) build

test: setup
	@uv sync --frozen --all-extras
	$(PYTEST)


install: build
	$(UV) pip install dist/*.whl

clean:
	rm -rf $(VENV) dist *.egg-info .pytest_cache __pycache__ .mypy_cache
