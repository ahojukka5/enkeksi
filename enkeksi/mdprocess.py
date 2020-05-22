import sqlite3
import sys
import shlex
import argparse
from tabulate import tabulate


def get_cursor():
    connection = sqlite3.connect(":memory:")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    return cursor


def parse_header(s: str):
    header = dict()
    for arg in shlex.split(s.strip("`")):
        s = arg.split("=")
        if len(s) == 1:
            header[s[0]] = True
        else:
            header[s[0]] = s[1]
    return header


def parse_args(line: str):
    parser = argparse.ArgumentParser("argsparser")
    sf = "store_false"
    parser.add_argument("--hide-input", dest="show_input", action=sf)
    parser.add_argument("--hide-output", dest="show_output", action=sf)
    parser.add_argument("--caption")
    parser.add_argument("--table-format", dest="tablefmt", default="psql")
    parser.add_argument("--hide-headers", dest="show_headers", action=sf)
    return parser.parse_known_args(shlex.split(line))


def process(cursor, block: str, file=sys.stdout):
    """ Given sqlite cursor object and a block, evaluate it and return
    results to output. """

    block = block.strip()

    if block.startswith("```sql"):
        assert block.endswith("```")
        ind1 = block.find('\n')
        ind2 = block.rfind('\n')
        code = block[ind1+1:ind2]
        args, _ = parse_args("")
        if code.startswith("--"):
            ind1 = code.find('\n')
            args, u = parse_args(code[:ind1])
            code = code[ind1+1:]
            if len(u) > 0:
                print("**Unknown arguments**: %s\n" % " ".join(u), file=file)

        if args.show_input:
            input_str = "```sql\n%s\n```" % code
            print(input_str, file=file)

        try:
            if code.count(';') > 1:
                cursor.executescript(code)
            else:
                cursor.execute(code)
        except Exception as err:
            msg = "Failed to execute SQL query:"
            print("\n```text\n%s\n\n%s" % (msg, code), file=file)
            print("\nError message: %s\n```" % str(err), file=file)
            return

        result = cursor.fetchall()

        if result and args.show_output:
            caption = "%s\n\n" % args.caption if args.caption else ""
            headers = result[0].keys() if args.show_headers else []
            srep = tabulate(result, headers=headers, tablefmt=args.tablefmt)
            output_str = "```text\n%s%s\n```" % (caption, srep)
            if args.show_input:
                print(file=file)
            print(output_str, file=file)
            print(file=file)

    else:
        print(block, file=file)
        print(file=file)
