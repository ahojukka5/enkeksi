import sqlite3
import sys
import shlex
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


def process(cursor, block: str, file=sys.stdout):
    """ Given sqlite cursor object and a block, evaluate it and return
    results to output. """

    block = block.strip()

    if block.startswith("```sql"):
        assert block.endswith("```")
        ind1 = block.find('\n')
        ind2 = block.rfind('\n')
        code = block[ind1+1:ind2]
        header = parse_header(block[:ind1])

        show_input = "hide_input" not in header
        if show_input:
            input_str = "```sql\n%s\n```" % code
            print(input_str, file=file)

        try:
            if "block" in header or code.count(';') > 1:
                cursor.executescript(code)
            else:
                cursor.execute(code)
        except Exception as err:
            msg = "Failed to execute SQL query:"
            print("\n```text\n%s\n\n%s" % (msg, code), file=file)
            print("\nError message: %s\n```" % str(err), file=file)
            return

        result = cursor.fetchall()

        show_output = result and "hide_output" not in header
        if show_output:
            caption = ""
            if "caption" in header:
                caption = "%s\n\n" % header["caption"]
            tablefmt = header.get("tablefmt", "psql")
            headers = result[0].keys() if "hide_headers" not in header else []
            srep = tabulate(result, headers=headers, tablefmt=tablefmt)
            output_str = "```text\n%s%s\n```" % (caption, srep)
            if show_input:
                print(file=file)
            print(output_str, file=file)
            print(file=file)

    else:
        print(block, file=file)
        print(file=file)
