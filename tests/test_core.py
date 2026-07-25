from __future__ import annotations

import sqlite3
from pathlib import Path

import pytest

from sqlfence import RenderOptions, SqlfenceError, render_markdown
from sqlfence.core import split_sql_statements, strip_generated_output


def test_renders_query_as_markdown_table() -> None:
    source = "# Movies\n\n```sql\nSELECT 1 AS one, 'two' AS word;\n```\n"
    rendered = render_markdown(source)
    assert "|   one | word" in rendered
    assert "|     1 | two" in rendered
    assert rendered.count("<!-- sqlfence:begin -->") == 1


def test_preserves_normal_markdown_and_blank_lines() -> None:
    source = "# Heading\n\nParagraph one.\n\nParagraph two.\n"
    assert render_markdown(source) == source


def test_hide_input_and_caption() -> None:
    source = """```sql
--hide-input --caption='Answer'
SELECT 42 AS value;
```
"""
    rendered = render_markdown(source)
    assert "SELECT 42" not in rendered
    assert "**Answer**" in rendered
    assert "42" in rendered


def test_info_string_directives() -> None:
    source = "```sql hide-input hide-headers\nSELECT 42 AS value;\n```\n"
    rendered = render_markdown(source)
    assert "SELECT" not in rendered
    assert "value" not in rendered
    assert "42" in rendered


def test_sqlfence_directive_comment() -> None:
    source = """```sql
-- sqlfence: hide-input caption='Count'
SELECT 2 AS value;
```
"""
    rendered = render_markdown(source)
    assert "**Count**" in rendered
    assert "SELECT" not in rendered


def test_legacy_enkeksi_directive_comment() -> None:
    source = """```sql
-- enkeksi: hide-input caption='Legacy'
SELECT 5 AS value;
```
"""
    rendered = render_markdown(source)
    assert "**Legacy**" in rendered
    assert "SELECT" not in rendered


def test_multiple_statements_share_connection() -> None:
    source = """```sql hide-input hide-output
CREATE TABLE movies(name TEXT);
INSERT INTO movies VALUES ('Fantasia');
```

```sql
SELECT name FROM movies;
```
"""
    rendered = render_markdown(source)
    assert "Fantasia" in rendered


def test_semicolon_inside_string_does_not_split_statement() -> None:
    statements = split_sql_statements("SELECT 'a;b' AS value; SELECT 2;")
    assert statements == ["SELECT 'a;b' AS value;", "SELECT 2;"]


def test_comments_do_not_break_statement_splitting() -> None:
    statements = split_sql_statements("SELECT 1 /* ; */; -- ;\nSELECT 2;")
    assert len(statements) == 2


def test_rendering_is_idempotent() -> None:
    source = "```sql\nSELECT 1 AS value;\n```\n"
    once = render_markdown(source)
    twice = render_markdown(once)
    assert twice == once


def test_strip_generated_output() -> None:
    source = "before\n<!-- sqlfence:begin -->\nold\n<!-- sqlfence:end -->\nafter\n"
    stripped = strip_generated_output(source)
    assert "old" not in stripped
    assert "before" in stripped and "after" in stripped


def test_legacy_enkeksi_marker_is_replaced() -> None:
    source = (
        "before\n<!-- enkeksi:begin -->\nold\n<!-- enkeksi:end -->\n"
        "```sql\nSELECT 6 AS value;\n```\n"
    )
    rendered = render_markdown(source)
    assert "old" not in rendered
    assert "<!-- sqlfence:begin -->" in rendered


def test_sql_error_has_source_line() -> None:
    source = "intro\n\n```sql\nSELCT 1;\n```\n"
    with pytest.raises(SqlfenceError, match="line 3"):
        render_markdown(source)


def test_keep_going_embeds_error() -> None:
    rendered = render_markdown(
        "```sql\nSELCT 1;\n```\n", RenderOptions(keep_going=True)
    )
    assert "sqlfence error:" in rendered


def test_unknown_directive_is_an_error() -> None:
    with pytest.raises(SqlfenceError, match="Unknown"):
        render_markdown("```sql unknown-option\nSELECT 1;\n```\n")


def test_check_executes_without_rendering() -> None:
    result = render_markdown("```sql\nSELECT 1;\n```\n", RenderOptions(check=True))
    assert result == ""


def test_file_database_is_read_only_by_default(tmp_path: Path) -> None:
    database = tmp_path / "data.sqlite"
    connection = sqlite3.connect(database)
    connection.execute("CREATE TABLE values_table(value INTEGER)")
    connection.commit()
    connection.close()

    source = "```sql\nINSERT INTO values_table VALUES (1);\n```\n"
    with pytest.raises(SqlfenceError, match="readonly"):
        render_markdown(source, RenderOptions(database=str(database)))


def test_file_database_can_be_written_explicitly(tmp_path: Path) -> None:
    database = tmp_path / "data.sqlite"
    source = "```sql hide-output\nCREATE TABLE data(value INTEGER);\n```\n"
    render_markdown(source, RenderOptions(database=str(database), read_only=False))
    connection = sqlite3.connect(database)
    assert connection.execute(
        "SELECT name FROM sqlite_master WHERE name='data'"
    ).fetchone()
    connection.close()


def test_unsupported_engine() -> None:
    with pytest.raises(SqlfenceError, match="Unsupported"):
        render_markdown("text", RenderOptions(engine="other"))


def test_unlabelled_fence_is_ignored() -> None:
    source = "```\nplain text\n```\n"
    assert render_markdown(source) == source
