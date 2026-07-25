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

The version 0.x first-line syntax remains supported. A preferred explicit form
is `-- enkeksi: hide-input caption='Result'`.

## Multiple statements

Statements are executed in order. Results from the last row-producing statement
in a block are rendered. Semicolons inside quoted strings and SQL comments do
not split statements.
