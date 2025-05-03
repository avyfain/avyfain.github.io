import argparse
import os

from pathlib import Path
from PIL import Image, ExifTags

# a = {v:k for k, v in ExifTags.TAGS.items()}
# a['DateTimeDigitized']
# > 36868

TIME_TAG = 36868


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input_dir', action='store', dest='input_dir', required=True)
    return parser.parse_args()


def main():
    args = parse_args()

    vals = {}

    p = Path(args.input_dir)
    for idx, f in enumerate(sorted(os.listdir(p))):
        if not f.endswith(('.jpg', '.jpeg')):
            continue
        img = Image.open(p / f)
        vals[f] = img.getexif().get(TIME_TAG, idx)

    file_order = sorted(vals, key=vals.get)

    for idx, f in enumerate(file_order):
        os.rename(p / f, p / f'{idx+1}_.jpg')

    for f in os.listdir(p):
        if f.endswith(('.jpg', '.jpeg')):
            os.rename(p / f, p / f.replace('_', ''))


if __name__ == '__main__':
    main()
