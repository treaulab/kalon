# kalon

An early-stage Python project.

## Status

Scaffolded: package, CLI, tests, and linting. No real functionality yet.

## Setup

```sh
uv sync
```

## Development

```sh
uv run kalon          # CLI (prints the version)
uv run pytest         # tests
uv run ruff check .   # lint
uv run ruff format .  # format
```

## Layout

- `src/kalon/` — package code
- `tests/` — tests
