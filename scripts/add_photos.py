# usage: add_photos.py -f FNAME [-n NUM_PHOTOS] [-y YEAR] [-m MONTH] [-d DAY]
# python scripts/add_photos.py -f OL17 -n 130
import os
import argparse
import random
from datetime import datetime

FRONT_MATTER = """
---
title: TBD
layout: photos
category: photos
main_image: {}/previews/{}.jpg
tags: [TBD]
photos:
{}
---
"""

FRONT_MATTER = FRONT_MATTER.strip()
PHOTO_STRING = ("  - url: {}/{}.jpg\n"
                "    preview_url: {}/previews/{}.jpg\n"
                "    caption: TBD")


def check_dir():
    assert os.getcwd().endswith('avyfain.github.io')


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--fname', action='store', dest='fname', required=True)
    parser.add_argument('-n', '--num_photos', action='store', dest='num_photos', type=int, default=20)
    parser.add_argument("-y", "--year", action="store", dest="year")
    parser.add_argument("-m", "--month", action="store", dest="month")
    parser.add_argument("-d", "--day", action="store", dest="day")

    return parser.parse_args()


def main():
    args = parse_args()
    yesterday = datetime.today()
    y = args.year if args.year else yesterday.strftime("%Y")
    m = args.month if args.month else yesterday.strftime("%m")
    d = args.day if args.day else yesterday.strftime("%d")
    n = args.num_photos + 1
    fname = args.fname
    thumbnail_idx = random.randint(1, n)

    photo_gen = (PHOTO_STRING.format(fname, i, fname, i) for i in range(1, n))

    with open('_posts/photos/{}-{}-{}-{}.md'.format(y, m, d, fname), 'w') as f:
        f.write(FRONT_MATTER.format(fname, thumbnail_idx, '\n'.join(photo_gen)))


if __name__ == '__main__':
    check_dir()
    main()
