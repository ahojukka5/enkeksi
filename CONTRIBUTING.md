# Contributing

## Setup

Install `uv`, clone the repository, and run:

```console
uv sync --all-groups
```

## Quality gates

Every change must pass:

```console
uv run ruff format --check .
uv run ruff check .
uv run mypy
uv run pytest
uv build
```

Keep commits focused and use an imperative subject line. Update tests and the
changelog for user-visible behavior. Pull requests should explain the problem,
the chosen solution, and the validation performed.
