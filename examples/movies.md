# Movie database

The first block creates temporary data and is omitted from rendered output.

```sql hide-input hide-output
CREATE TABLE movies(name TEXT, year INTEGER);
INSERT INTO movies VALUES ('Snow White', 1937), ('Fantasia', 1940);
```

```sql hide-input caption='Movies ordered by release year'
SELECT name, year FROM movies ORDER BY year;
```
