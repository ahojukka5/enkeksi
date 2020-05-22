# Assignment 1

```sql
--hide-input
CREATE TABLE Movies (id INTEGER PRIMARY KEY, name TEXT, year INTEGER);
INSERT INTO Movies (name, year) VALUES ("Snow White", 1937);
INSERT INTO Movies (name, year) VALUES ("Fantasia", 1940);
INSERT INTO Movies (name, year) VALUES ("Pinocchio", 1940);
INSERT INTO Movies (name, year) VALUES ("Dumbo", 1941);
INSERT INTO Movies (name, year) VALUES ("Bambi", 1942);
```

Create a query returning the names of the movies.

Keywords: **SELECT**

## Tables

### Movies

```sql
--hide-input --caption="Table: Movies"
SELECT * FROM Movies;
```

## Expected result

```text
+------------+
| name       |
|------------|
| Snow White |
| Fantasia   |
| Pinocchio  |
| Dumbo      |
| Bambi      |
+------------+
```

## Solution

```sql
SELECT
  name
FROM
  Movies;
```
