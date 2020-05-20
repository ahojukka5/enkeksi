#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import argparse
from markdown_sql_eval import process_file


def main(argv=None, file=sys.stdout):
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    args = parser.parse_args(argv or sys.argv[1:])
    process_file(args.filename, file)
