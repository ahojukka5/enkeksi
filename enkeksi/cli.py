#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import argparse
from enkeksi.mdprocess import get_cursor, process


def process_file(filename: str, database: str, file=sys.stdout):
    blocks = open(filename).read().split('\n\n')
    cursor = get_cursor(database)
    for block in blocks:
        process(cursor, block, file=file)


def main(argv=None, file=sys.stdout):
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    parser.add_argument('--database', default=':memory:')
    args = parser.parse_args(argv or sys.argv[1:])
    process_file(args.filename, args.database, file=file)
