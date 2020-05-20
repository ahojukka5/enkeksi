# Demo page

This demo page is processed using enkeksi. Original markdown can be found from
a GitHub repo, `docs/demo_tmpl.md`. Let's start with something what whould be
done in beginning of all software projects, "Hello World". The first line is
the actual markdown block, what you will be writing to the markdown file:

````markdown
```sql
SELECT "Hello", "World";
```
````

By doing this, the actual result is going to be:

```sql
SELECT "Hello", "World";
```

For the sake of clarity, the first block shown in this page is not going to be
visual in normal documentation, but is shown only for documentation purposes of
this package. In real case scenario, user writes the content of the first block
to the documentation which gets rendered to the second and third block.

A small "mini-language" is defined in the header row of the block which can be
used to alter the rendered result. By header row I mean the row starting with
the sql command with three back-ticks:

````markdown
```sql opt1 opt2 val1=val2 val3="a b c"  // <-- header row with options
(my sql query ...)
```
````

First of all, sometimes it's better not to have headers in tables. Those can be
supressed using `hide_headers`. So if you write the following to your markdown
file:

````markdown
```sql hide_headers
SELECT "Hello", "World";
```
````

The result will be the following:

```sql hide_headers
SELECT "Hello", "World";
```

You probably will have some setup sql queries what you don't want appear to the
documentation. These can be hidden using `hide_input`. For example, creating a
new table, without any output is done:

````markdown
```sql hide_input
CREATE TABLE Movies (id INTEGER PRIMARY KEY, name TEXT, year INTEGER);
INSERT INTO Movies (name, year) VALUES ("Snow White", 1937);
INSERT INTO Movies (name, year) VALUES ("Fantasia", 1940);
INSERT INTO Movies (name, year) VALUES ("Pinocchio", 1940);
INSERT INTO Movies (name, year) VALUES ("Dumbo", 1941);
INSERT INTO Movies (name, year) VALUES ("Bambi", 1942);
```
````

```sql hide_input
CREATE TABLE Movies (id INTEGER PRIMARY KEY, name TEXT, year INTEGER);
INSERT INTO Movies (name, year) VALUES ("Snow White", 1937);
INSERT INTO Movies (name, year) VALUES ("Fantasia", 1940);
INSERT INTO Movies (name, year) VALUES ("Pinocchio", 1940);
INSERT INTO Movies (name, year) VALUES ("Dumbo", 1941);
INSERT INTO Movies (name, year) VALUES ("Bambi", 1942);
```

This way, the table will be there ready for demonstration, but the actual sql
query is not rendered to the final documentation. The sql query was executed
in above, but it's invisible in the documentation. So, if we write the
following to our markdown file:

````markdown
```sql
SELECT * FROM Movies;
```
````

We get the following result:

```sql
SELECT * FROM Movies;
```

Keep on mind, that the first block is just to show what does the block look
like in markdown file. Technically, it's a markdown block. In your final
documentation, you can safely skip those.

There might be cases where you don't want to render the actual query performed,
but get only results. That can be doing with `hide_input` command:

````markdown
```sql hide_input
SELECT * FROM Movies;
```
````

As a result, you don't find the SQL query from the final documentation, only the
result:

```sql hide_input
SELECT * FROM Movies;
```

Respectively there is `hide_output` but it's unsure where to use that. With
that option, the executed sql query is rendered to the final document, but the
result is not.

It's possible to add a caption to the query, using `caption="my text"`, i.e.

````markdown
```sql caption="Table: Movies"
SELECT * FROM Movies;
```
````

The result of this is:

```sql caption="Table: Movies"
SELECT * FROM Movies;
```

Different options can be freely combined, so for example the following will work:

````markdown
```sql hide_input caption="Table: Movies"
SELECT * FROM Movies;
```
````

```sql hide_input caption="Table: Movies"
SELECT * FROM Movies;
```
