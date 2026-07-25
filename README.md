# enkeksi

[![CI](https://github.com/ahojukka5/enkeksi/actions/workflows/ci.yml/badge.svg)](https://github.com/ahojukka5/enkeksi/actions/workflows/ci.yml)
[![PyPI](https://img.shields.io/pypi/v/enkeksi.svg)](https://pypi.org/project/enkeksi/)
[![Python](https://img.shields.io/pypi/pyversions/enkeksi.svg)](https://pypi.org/project/enkeksi/)

**Executable SQL examples for ordinary Markdown files.**

`enkeksi` finds fenced `sql` blocks, executes them against SQLite or DuckDB,
and writes the results back as Markdown tables. It is intentionally smaller
than a notebook system: Markdown goes in and Markdown comes out.

## Install

```console
uv tool install enkeksi
```

DuckDB support is optional:

```console
uv tool install 'enkeksi[duckdb]'
```

## Example

Create `report.md`:

````markdown
# Movies

```sql
CREATE TABLE movies(name TEXT, year INTEGER);
INSERT INTO movies VALUES ('Snow White', 1937), ('Fantasia', 1940);
```

```sql
--hide-input --caption='Movies in the database'
SELECT * FROM movies ORDER BY year;
```
````

Render it:

```console
enkeksi report.md --output report-rendered.md
```

Use `--check` in CI to verify every SQL example without creating output:

```console
enkeksi report.md --check
```

File-backed databases are opened read-only unless `--write` is explicitly
provided. The historical command name `markdown-sql-eval` remains available as
an alias.

## Directives

Directives can be placed in the fence info string:

````markdown
```sql hide-input hide-headers caption='Result'
SELECT 42 AS answer;
```
````

The compatible first-line syntax is also supported:

```sql
--hide-input --caption='Result' --table-format=github
```

Available directives are `hide-input`, `hide-output`, `hide-headers`,
`caption`, and `table-format`.

## Development

```console
uv sync --all-groups
uv run ruff check .
uv run mypy
uv run pytest
uv build
```

See the full documentation and [CHANGELOG.md](CHANGELOG.md) for details.
