import argparse
import os

from pathlib import Path


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input_dir', action='store', dest='input_dir', required=True)
    return parser.parse_args()


def main():
    args = parse_args()
    p = Path(args.input_dir)
    for idx, f in enumerate(sorted(os.listdir(p))):
        if not f.endswith(('.jpg', '.jpeg')):
            continue
        new_f = f'{idx + 1}.jpeg'
        os.rename(p / f, p / new_f)

if __name__ == '__main__':
    main()
