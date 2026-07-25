# Migration from 0.x

Version 1.0 retains the old `markdown-sql-eval` command and first-line directives. Existing templates should normally continue to render.

Behavior changes:

- Python 3.10 or newer is required.
- SQL errors now cause a non-zero exit status.
- File databases are read-only by default; use `--write` only when database changes are intended.
- Markdown tables are the default output format.
- Generated output uses markers so `--in-place` remains idempotent.
