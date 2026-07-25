from __future__ import annotations

import io
from pathlib import Path

from sqlfence.cli import main


def test_cli_reads_stdin_and_writes_stdout() -> None:
    stdout = io.StringIO()
    exit_code = main(
        ["-"],
        stdin=io.StringIO("```sql\nSELECT 7 AS value;\n```\n"),
        stdout=stdout,
    )
    assert exit_code == 0
    assert "7" in stdout.getvalue()


def test_cli_check_returns_failure_for_invalid_sql() -> None:
    stderr = io.StringIO()
    exit_code = main(
        ["-", "--check"], stdin=io.StringIO("```sql\nBAD SQL;\n```\n"), stderr=stderr
    )
    assert exit_code == 1
    assert "sqlfence:" in stderr.getvalue()


def test_cli_writes_output_file(tmp_path: Path) -> None:
    source = tmp_path / "input.md"
    target = tmp_path / "output.md"
    source.write_text("```sql\nSELECT 3;\n```\n", encoding="utf-8")
    assert main([str(source), "--output", str(target)]) == 0
    assert "3" in target.read_text(encoding="utf-8")


def test_cli_in_place_is_idempotent(tmp_path: Path) -> None:
    source = tmp_path / "input.md"
    source.write_text("```sql\nSELECT 9;\n```\n", encoding="utf-8")
    assert main([str(source), "--in-place"]) == 0
    once = source.read_text(encoding="utf-8")
    assert main([str(source), "--in-place"]) == 0
    assert source.read_text(encoding="utf-8") == once
