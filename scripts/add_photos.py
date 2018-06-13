# usage: add_photos.py -f FNAME [-n NUM_PHOTOS] [-y YEAR] [-m MONTH] [-d DAY]
# for the whole thing:
#
# python scripts/resize_photos.py -i ../fotos/XXX/
# python scripts/upload_to_s3.py -i ../fotos/XXX/
# python scripts/add_photos.py -i ../fotos/XXX/

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

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-f', '--fname', action='store', dest='fname')
    group.add_argument('-i', '--inputdir', action='store', dest='inputdir')
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

    if args.inputdir.endswith('/'):
        in_dir = args.inputdir[:-1]

    n = len(os.listdir(in_dir))
    fname = os.path.split(in_dir)[-1]

    if args.fname:
        fname = args.fname

    thumbnail_idx = random.randint(1, n)

    photo_gen = (PHOTO_STRING.format(fname, i, fname, i) for i in range(1, n))

    with open('_posts/photos/{}-{}-{}-{}.md'.format(y, m, d, fname), 'w') as f:
        f.write(FRONT_MATTER.format(fname, thumbnail_idx, '\n'.join(photo_gen)))


if __name__ == '__main__':
    check_dir()
    main()
