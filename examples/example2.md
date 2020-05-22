# Sample file

Hello, this is a sample file. Below, we initialize some test data to sqlite
database. It doesn't show in the final output, because of `--hide-input` flag.

```sql
--hide-input
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
