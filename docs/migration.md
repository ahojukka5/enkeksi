# Migration from enkeksi 0.x

The project and distribution are now named `sqlfence`. Install the new package
and use the new command and import path:

```console
uv tool install sqlfence
sqlfence input.md --output output.md
```

```python
from sqlfence import RenderOptions, SqlfenceError, render_markdown
```

The historical `enkeksi` and `markdown-sql-eval` executables remain aliases.
Existing `-- enkeksi:` directives and `<!-- enkeksi:begin/end -->` generated
regions are recognized, then rendered using the new `sqlfence` markers.
`EnkeksiError` remains an alias of `SqlfenceError` in the new Python API.

Other behavior changes from 0.x:

- Python 3.10 or newer is required.
- SQL errors produce a non-zero exit status.
- File databases are read-only by default; use `--write` only when changes are intended.
- Markdown tables are the default output format.
