# Getting started

## Installation

```console
uv tool install enkeksi
```

For a project dependency:

```console
uv add --dev enkeksi
```

## Render a document

```console
enkeksi input.md --output output.md
```

Use an in-memory SQLite database by default. Blocks in the same document share
one connection, so setup statements are visible to later queries.

## Validate in CI

```console
enkeksi docs/database.md --check
```

The command exits non-zero when parsing or SQL execution fails.
