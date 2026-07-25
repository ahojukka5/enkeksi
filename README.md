# sqlfence

[![CI](https://github.com/ahojukka5/sqlfence/actions/workflows/ci.yml/badge.svg)](https://github.com/ahojukka5/sqlfence/actions/workflows/ci.yml)
[![PyPI](https://img.shields.io/pypi/v/sqlfence.svg)](https://pypi.org/project/sqlfence/)
[![Python](https://img.shields.io/pypi/pyversions/sqlfence.svg)](https://pypi.org/project/sqlfence/)

**Executable SQL examples for ordinary Markdown files.**

`sqlfence` finds fenced `sql` blocks, executes them against SQLite or DuckDB,
and writes the results back as Markdown tables. It is intentionally smaller
than a notebook system: Markdown goes in and Markdown comes out.

## Install

```console
uv tool install sqlfence
```

DuckDB support is optional:

```console
uv tool install 'sqlfence[duckdb]'
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
sqlfence report.md --output report-rendered.md
```

Use `--check` in CI to verify every SQL example without creating output:

```console
sqlfence report.md --check
```

File-backed databases are opened read-only unless `--write` is explicitly
provided. The historical command names `enkeksi` and `markdown-sql-eval`
remain available as migration aliases.

## Directives

Directives can be placed in the fence info string:

````markdown
```sql hide-input hide-headers caption='Result'
SELECT 42 AS answer;
```
````

The preferred explicit first-line form is:

```sql
-- sqlfence: hide-input caption='Result' table-format=github
```

Legacy `-- enkeksi:` directives are also recognized. Available directives are
`hide-input`, `hide-output`, `hide-headers`, `caption`, and `table-format`.

## Development

```console
uv sync --all-groups
uv run ruff check .
uv run mypy
uv run pytest
uv build
```

See the full documentation and [CHANGELOG.md](CHANGELOG.md) for details.
