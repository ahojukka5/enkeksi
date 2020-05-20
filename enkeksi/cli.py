#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import argparse
from enkeksi.mdprocess import get_cursor, process


def process_file(filename: str, file=sys.stdout):
    blocks = open(filename).read().split('\n\n')
    cursor = get_cursor()
    for block in blocks:
        process(cursor, block, file=file)


def main(argv=None, file=sys.stdout):
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    args = parser.parse_args(argv or sys.argv[1:])
    process_file(args.filename, file=file)
