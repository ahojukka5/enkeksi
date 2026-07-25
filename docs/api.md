# Python API

```python
from enkeksi import RenderOptions, render_markdown

rendered = render_markdown(
    source,
    RenderOptions(database="examples.sqlite", read_only=True),
)
```

## `render_markdown(markdown, options=None)`

Executes every SQL fence and returns rendered Markdown. It raises
`EnkeksiError` on the first failure unless `keep_going=True`.

## `RenderOptions`

- `engine`: `sqlite` or `duckdb`.
- `database`: database path or `:memory:`.
- `read_only`: explicit mode; when omitted, file databases are read-only.
- `keep_going`: embed errors instead of raising immediately.
- `check`: execute without returning rendered content.
- `default_table_format`: default `tabulate` format.
