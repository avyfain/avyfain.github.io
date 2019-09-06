# usage: draft.py -f FNAME
from __future__ import absolute_import

import os
import argparse
from datetime import datetime

FRONT_MATTER = """
---
title: "TBD"
main_image: TBD.jpg
tags: []
layout: post
category: articles
description: TBD
---
"""

FRONT_MATTER = FRONT_MATTER.strip()


def check_dir():
    assert os.getcwd().endswith('avyfain.github.io')


def parse_args():
    parser = argparse.ArgumentParser()

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-f', '--fname', action='store', dest='fname')
    parser.add_argument("-y", "--year", action="store", dest="year")
    parser.add_argument("-m", "--month", action="store", dest="month")
    parser.add_argument("-d", "--day", action="store", dest="day")

    return parser.parse_args()


def main():
    args = parse_args()
    today = datetime.today()
    y = args.year if args.year else today.strftime("%Y")
    m = args.month if args.month else today.strftime("%m")
    d = args.day if args.day else today.strftime("%d")

    fname = args.fname if args.fname else 'TBD'

    full_path = '_drafts/{}-{}-{}-{}.md'.format(y, m, d, fname)
    with open(full_path, 'w') as f:
        f.write(FRONT_MATTER)
    print("Successfully generated a post at", full_path)


if __name__ == '__main__':
    check_dir()
    main()
