# SQL blocks

Any CommonMark fenced block whose language is `sql` is executable.

````markdown
```sql
SELECT 1 AS value;
```
````

## Directives

Use directives after `sql` in the fence information string:

````markdown
```sql hide-input caption='Current users' table-format=github
SELECT id, name FROM users ORDER BY id;
```
````

| Directive | Effect |
| --- | --- |
| `hide-input` | Omit SQL from rendered Markdown. |
| `hide-output` | Execute SQL but omit its result. |
| `hide-headers` | Omit column headings. |
| `caption='Text'` | Add a bold caption above the result. |
| `table-format=github` | Select a `tabulate` output format. |

The preferred explicit first-line form is
`-- sqlfence: hide-input caption='Result'`. The legacy `-- enkeksi:` form is
also supported.

## Generated output markers

Rendered regions use `<!-- sqlfence:begin -->` and
`<!-- sqlfence:end -->`. Legacy `enkeksi` regions are removed and replaced on
the next render, preserving idempotent in-place updates.

## Multiple statements

Statements are executed in order. Results from the last row-producing statement
in a block are rendered. Semicolons inside quoted strings and SQL comments do
not split statements.
