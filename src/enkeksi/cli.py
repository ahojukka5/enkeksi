"""Command-line interface for enkeksi."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Sequence, TextIO

from . import __version__
from .core import EnkeksiError, RenderOptions, render_markdown


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="enkeksi",
        description="Execute SQL fenced blocks in Markdown and render the results.",
    )
    parser.add_argument("input", help="Input Markdown file, or - for standard input")
    output = parser.add_mutually_exclusive_group()
    output.add_argument("-o", "--output", help="Write rendered Markdown to this file")
    output.add_argument(
        "--in-place", action="store_true", help="Replace the input file atomically"
    )
    parser.add_argument("--database", default=":memory:", help="Database path")
    parser.add_argument(
        "--engine", choices=("sqlite", "duckdb"), default="sqlite"
    )
    parser.add_argument(
        "--write",
        action="store_true",
        help="Allow writes to a file-backed database (read-only by default)",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Execute every SQL block without producing rendered Markdown",
    )
    parser.add_argument(
        "--keep-going",
        action="store_true",
        help="Render SQL errors into the document instead of exiting immediately",
    )
    parser.add_argument(
        "--table-format", default="github", help="Default tabulate table format"
    )
    parser.add_argument(
        "--version", action="version", version=f"%(prog)s {__version__}"
    )
    return parser


def _read_input(filename: str, stdin: TextIO) -> str:
    if filename == "-":
        return stdin.read()
    return Path(filename).read_text(encoding="utf-8")


def _write_atomic(path: Path, content: str) -> None:
    temporary = path.with_suffix(path.suffix + ".enkeksi.tmp")
    temporary.write_text(content, encoding="utf-8")
    temporary.replace(path)


def main(
    argv: Sequence[str] | None = None,
    *,
    stdin: TextIO = sys.stdin,
    stdout: TextIO = sys.stdout,
    stderr: TextIO = sys.stderr,
) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.in_place and args.input == "-":
        parser.error("--in-place cannot be used with standard input")

    try:
        markdown = _read_input(args.input, stdin)
        rendered = render_markdown(
            markdown,
            RenderOptions(
                engine=args.engine,
                database=args.database,
                read_only=False if args.write else None,
                keep_going=args.keep_going,
                check=args.check,
                default_table_format=args.table_format,
            ),
        )
    except (OSError, EnkeksiError) as error:
        print(f"enkeksi: {error}", file=stderr)
        return 1

    if args.check:
        return 0
    if args.in_place:
        _write_atomic(Path(args.input), rendered)
    elif args.output:
        Path(args.output).write_text(rendered, encoding="utf-8")
    else:
        stdout.write(rendered)
    return 0


def entrypoint() -> None:
    raise SystemExit(main())


if __name__ == "__main__":
    entrypoint()
