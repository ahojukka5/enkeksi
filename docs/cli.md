# Command line

```text
sqlfence INPUT [--output FILE | --in-place] [options]
```

`INPUT` may be `-` for standard input. Without an output option, rendered
Markdown is written to standard output.

## Important options

- `--database PATH`: use a file-backed database.
- `--engine sqlite|duckdb`: choose the database engine.
- `--write`: allow modifying a file-backed database.
- `--check`: execute all blocks without rendering output.
- `--keep-going`: embed errors and continue with later blocks.
- `--table-format FORMAT`: change the default `tabulate` format.

The historical `enkeksi` and `markdown-sql-eval` executables are retained as
migration aliases. Their help and version output identify the program as
`sqlfence`.
