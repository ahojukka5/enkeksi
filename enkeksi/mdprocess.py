import sqlite3
import sys
import tabulate


def get_cursor():
    connection = sqlite3.connect(":memory:")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    return cursor


def process(cursor, block: str, file=sys.stdout, show_headers=True):
    """ Given sqlite cursor object and a block, evaluate it and return
    results to output. """

    block = block.strip()

    if block.startswith("```sql"):
        assert block.endswith("```")
        ind1 = block.find('\n')
        ind2 = block.rfind('\n')
        code = block[ind1+1:ind2]
        first_line = block[:ind1]

        if "block" in first_line or code.count(';') > 1:
            cursor.executescript(code)
        else:
            cursor.execute(code)
        result = cursor.fetchall()

        show_input = "hide_input" not in first_line
        show_output = result and "hide_output" not in first_line

        if show_input:
            input_str = "```sql\n%s\n```" % code
            print(input_str, file=file)

        if show_output:
            headers = result[0].keys() if show_headers else []
            srep = tabulate.tabulate(result, headers=headers, tablefmt="psql")
            output_str = "```text\n%s\n```" % srep
            if show_input:
                print(file=file)
            print(output_str, file=file)
            print(file=file)

    else:
        print(block, file=file)
        print(file=file)
