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
    return tuple((x - y) // 2 for x, y in zip(a, b))

def main():
    args = parse_args()
	target_dir = Path(args.out_dir)

	for idx, i in enumerate(os.listdir(args.input_dir)):
	    img = Image.open(i)
	    border = get_border_size(img)
	    img = ImageOps.expand(img, border=border, fill="white")
	    img.save(target_dir / Path(f'{idx +1}.jpeg'))


if __name__ == '__main__':
    main()
