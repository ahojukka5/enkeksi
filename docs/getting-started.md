# Getting started

## Installation

```console
uv tool install sqlfence
```

For a project dependency:

```console
uv add --dev sqlfence
```

DuckDB support is available through the optional extra:

```console
uv add 'sqlfence[duckdb]'
```

## Render a document

```console
sqlfence input.md --output output.md
```

Use an in-memory SQLite database by default. Blocks in the same document share
one connection, so setup statements are visible to later queries.

## Validate in CI

```console
sqlfence docs/database.md --check
```

The command exits non-zero when parsing or SQL execution fails.
