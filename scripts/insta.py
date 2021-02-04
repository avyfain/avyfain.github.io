import argparse
import os
from pathlib import Path
from PIL import Image, ImageOps

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input_dir', action='store', dest='input_dir', required=True)
    parser.add_argument('-o', '--out_dir', action='store', dest='out_dir', required=True)
    return parser.parse_args()

def get_border_size(img):
    a = [max(img.size)]*2
    b = img.size
    square_border = tuple((x - y) // 2 for x, y in zip(a, b))
    padding = tuple(int(sum(x)) for x in zip([max(img.size) * .05]*2, square_border))
    return padding

def main():
    args = parse_args()
    input_dir = Path(args.input_dir)
    target_dir = Path(args.out_dir)
    target_dir.mkdir(parents=True, exist_ok=True)

    for idx, i in enumerate(os.listdir(input_dir)):
        img = Image.open(input_dir / Path(i))
        border = get_border_size(img)
        img = ImageOps.expand(img, border=border, fill="white")
        img.save(target_dir / Path(f'{idx +1}.jpeg'))


if __name__ == '__main__':
    main()
