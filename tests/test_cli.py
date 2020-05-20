import textwrap
import io
import os
from enkeksi.cli import main


def test_main(tmpdir):
    fh = tmpdir.join("hello.md")
    content = textwrap.dedent("""
    # Hello, world!

    ```sql
    SELECT 1+1;
    ```
    """).strip()

    fh.write(content)
    filename = os.path.join(fh.dirname, fh.basename)
    output = io.StringIO()
    main([filename], file=output)
    assert "2" in output.getvalue()
