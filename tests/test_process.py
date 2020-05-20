import io
import textwrap
import pytest

from enkeksi import get_cursor, process


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
