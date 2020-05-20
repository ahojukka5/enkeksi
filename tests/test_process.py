import io
import textwrap
import pytest

from enkeksi.mdprocess import get_cursor, process, parse_header


@pytest.fixture
def cursor():
    return get_cursor()


@pytest.fixture
def output():
    return io.StringIO()


def test_process(cursor, output):
    block = textwrap.dedent("""
    ```sql
    SELECT 1+1;
    ```
    """)
    process(cursor, block, output, show_headers=False)
    assert "2" in output.getvalue()


def test_process_caption(cursor, output):
    block = textwrap.dedent("""
    ```sql caption="hello"
    SELECT 1+1;
    ```
    """)
    process(cursor, block, output, show_headers=False)
    assert "hello" in output.getvalue()


def test_process_failure(cursor, output):
    block = textwrap.dedent("""
    ```sql
    SELCT 1+1;
    ```
    """)
    process(cursor, block, output, show_headers=False)
    print("test_process_failure")
    print(output.getvalue())
    print("test_process_failure end")
    assert "Error" in output.getvalue()


def test_process_normal_text(cursor, output):
    block = textwrap.dedent("""
    Hello, World!
    """)
    process(cursor, block, output, show_headers=False)
    assert "Hello" in output.getvalue()


def test_block_process(cursor, output):
    block = textwrap.dedent("""
    ```sql
    CREATE TABLE Foo (id INTEGER PRIMARY KEY, data INTEGER);
    INSERT INTO Foo (data) VALUES (1);
    ```
    """)
    process(cursor, block, output, show_headers=False)
    cursor.execute("SELECT * FROM Foo")
    assert len(cursor.fetchall()) == 1


def test_parse_header():
    s = '```sql hide_input caption="Hello World"'
    p = parse_header(s)
    assert 'sql' in p
    assert 'hide_input' in p
    assert 'caption' in p
    assert p["caption"] == "Hello World"
