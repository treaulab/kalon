# dreamer

Early-stage Python project. See `README.md` for the current status.

## Commands

- `uv sync` — install dependencies
- `uv run dreamer` — CLI
- `uv run pytest` — tests
- `uv run ruff check .` — lint
- `uv run ruff format .` — format

## Conventions

- Python ≥3.12, `src/` layout, type hints on public functions.
- Keep dependencies minimal; add runtime deps with `uv add`, dev deps with `uv add --dev`.
- Tests live in `tests/`; run them before claiming a change is done.
- Never commit secrets or local env files. `.env` is ignored; use `.env.example` when the first secret appears.
- Commits: single-line conventional-commit subjects.
