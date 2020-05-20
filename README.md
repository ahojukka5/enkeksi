# enkeksi - Markdown-SQL evaluator

[![Python CI][ci-img]][ci-url]
[![Coverate Status][coveralls-img]][coveralls-url]
[![Documentation Status][documentation-img]][documentation-url]

Package author: Jukka Aho (@ahojukka5, ahojukka5@gmail.com)

enkeksi takes a markdown-formatted input and executes the sql queries found in
it, and returns a markdown-formatted output where the results of the sql queries
have been added. Package can be used, for example, to create a dynamic project
documentation where SQL queries are automatically executed to get example
results in a dynamic manner. This way it is easy to spot from the non-working
documentation is there is problems with the database.

enkeksi comes with a command line tool `markdown-sql-eval` which can be used
to process markdown files efficiently.

Project is hosted in GitHub: <https://github.com/ahojukka5/enkeksi>.

Documentation is hotes in ReadTheDocs: <https://enkeksi.readthedocs.io/>.

## Installing package

To install the most recent package from Python Package Index (PyPi), use git:

```bash
pip install enkeksi
```

To install the development version, you can install the package directly from
the GitHub:

```bash
pip install git+git://github.com/ahojukka5/enkeksi.git
```

## CLI Usage

Consider the following demo markdown file:

````markdown
# Sample file

Hello, this is a sample file. Below, we initialize some test data to sqlite
database. It doesn't show in the final output, because of `hide_input` flag.

```sql hide_input
CREATE TABLE Movies (id INTEGER PRIMARY KEY, name TEXT, year INTEGER);
INSERT INTO Movies (name, year) VALUES ("Snow White", 1937);
INSERT INTO Movies (name, year) VALUES ("Fantasia", 1940);
```

To list the content of the database, we need to use `SELECT` in SQL query:

```sql
SELECT * FROM Movies;
```

The total number of rows in database is:

```sql
SELECT COUNT(*) AS 'Number of movies in database' FROM Movies;
```
````

Processing the file with `markdown-sql-eval`:

```bash
markdown-sql-eval examples/example2.md
```

Result is:

````markdown
# Sample file

Hello, this is a sample file. Below, we initialize some test data to sqlite
database. It doesn't show in the final output, because of `hide_input` flag.

To list the content of the database, we need to use `SELECT` in SQL query:

```sql
SELECT * FROM Movies;
```

```text
+------+------------+--------+
|   id | name       |   year |
|------+------------+--------|
|    1 | Snow White |   1937 |
|    2 | Fantasia   |   1940 |
+------+------------+--------+
```

The total number of rows in database is:

```sql
SELECT COUNT(*) AS 'Number of movies in database' FROM Movies;
```

```text
+--------------------------------+
|   Number of movies in database |
|--------------------------------|
|                              2 |
+--------------------------------+
```
````

The generated markdown file can then be added to your project documentation
and hosted using e.g. mkdocs.

## Contributing

Contributions are welcome as usual. If you have any good idea, and especially,
a better name for a package, raise an issue.

[ci-img]: https://github.com/ahojukka5/enkeksi/workflows/Python%20CI/badge.svg
[ci-url]: https://github.com/ahojukka5/enkeksi/actions
[coveralls-img]: https://coveralls.io/repos/github/ahojukka5/enkeksi/badge.svg?branch=master
[coveralls-url]: https://coveralls.io/github/ahojukka5/enkeksi?branch=master
[documentation-img]: https://readthedocs.org/projects/enkeksi/badge/?version=latest
[documentation-url]: https://enkeksi.readthedocs.io/en/latest/?badge=latest
