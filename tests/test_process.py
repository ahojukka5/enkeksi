import io
import textwrap
from enkeksi import get_cursor, process


def test_process():
    output = io.StringIO()
    block = textwrap.dedent("""
    ```sql
    SELECT 1+1;
    ```
    """)
    cursor = get_cursor()
    process(cursor, block, output, show_headers=False)
    assert "2" in output.getvalue()
