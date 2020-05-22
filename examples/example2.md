# Sample file

Hello, this is a sample file. Below, we initialize some test data to sqlite
database. It doesn't show in the final output, because of `--hide-input` flag.

```sql
--hide-input
CREATE TABLE Movies (id INTEGER PRIMARY KEY, name TEXT, year INTEGER);
INSERT INTO Movies (name, year) VALUES ("Snow White", 1937);
INSERT INTO Movies (name, year) VALUES ("Fantasia", 1940);
```

To list the content of the database, we need to use `SELECT` in SQL query. We
can use extra directive `--caption='Table: Movies'` to add caption to output:

```sql
--hide-input --caption='Table: Movies'
SELECT * FROM Movies;
```

SQL results are formatted using [tabulate](https://pypi.org/project/tabulate/).
Using directive `--table-format` we can change how the end results looks like.
By default, `psgl` is used and there rest options can be found from tabulate's
documentation. The total number of rows in database is:

```sql
--caption='With psql formatting'
SELECT COUNT(*) AS 'Number of movies in database' FROM Movies;
```

Directive `--hide-headers` can be used to hide the header row of the result.

```sql
--table-format='github' --hide-headers --caption='With github formatting and headers removed'
SELECT COUNT(*) AS 'Now shown' FROM Movies;
```
