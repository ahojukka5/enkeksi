# enkeksi

`enkeksi` executes SQL fenced code blocks in ordinary Markdown and inserts the
results as Markdown tables. It is designed for tested database documentation,
README examples, generated reports, and CI checks.

## Design goals

- **Plain files:** Markdown in, Markdown out.
- **Reproducible:** every SQL example is executable in CI.
- **Safe defaults:** file databases are read-only unless writes are requested.
- **Small surface:** no notebook server, kernel, or browser runtime.
- **Idempotent:** generated sections are replaced rather than duplicated.
