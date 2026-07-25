# Changelog

All notable changes are documented here. The project follows Semantic Versioning.

## 1.0.0 - 2026-07-25

### Added

- Robust CommonMark parsing using `markdown-it-py`.
- Idempotent generated-output regions for safe in-place rendering.
- SQLite support with read-only file databases by default.
- Optional DuckDB support through the `duckdb` extra.
- `enkeksi` CLI with stdin/stdout, output files, atomic `--in-place`, `--check`,
  `--keep-going`, and explicit `--write` modes.
- Typed public Python API.
- Modern `uv` project, Ruff, mypy, pytest, coverage, MkDocs, CI, and trusted
  PyPI publishing workflow.

### Changed

- SQL query results are Markdown tables by default.
- SQL failures now produce a non-zero CLI exit code by default.
- The package requires Python 3.10 or newer.

### Compatibility

- The historical `markdown-sql-eval` command remains as an alias.
- Version 0.x first-line directives remain supported.
