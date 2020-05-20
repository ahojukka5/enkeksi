# Welcome to enkeksi's documentation

enkeksi takes a markdown-formatted input and executes the sql queries found in
it, and returns a markdown-formatted output where the results of the sql queries
have been added. Package can be used, for example, to create a dynamic project
documentation where SQL queries are automatically executed to get example
results in a dynamic manner. This way it is easy to spot from the non-working
documentation is there is problems with the database.

As a proof of concept, this project documentation itself is generated from a
markdown file `docs/index.md` using the tools provided in this package.
Documentation is built using mkdocs and hosted in readthedocs.io.

The basic idea is that user can write typical sql queries to the project
documentation, using markdown format, for example:

````markdown
```sql
SELECT 1+1;
```
````

In usual scenario, this get's rendered in the following way:

```sql
SELECT 1+1;
```

However, using enkeksi's functionalities, it's possible to actually run that
query and add the results to the markdown, automatically.

Package is having a function `enkeksi.mdprocess.process` which is used
internally, but the focus is on a command-line tool. So, let's assume that user
is having the following markdown file, call it `hello_template.md`:

````markdown
# Hello world

This is my text.

This is my SQL query:

```sql
SELECT 1+1;
```
````

Using command line tool `markdown-sql-eval`, one can create a new version of
file having that sql query evaluated:

```bash
markdown-sql-eval hello_template.md > hello.md
```

The resulting file content is:

````markdown
# Hello world

This is my text.

This is my SQL query:

```sql
SELECT 1+1;
```

```text
+-------+
|   1+1 |
|-------|
|     2 |
+-------+
```
````

In Demo page you will find some examples how to fine-tune the output of the
preprocessor.
