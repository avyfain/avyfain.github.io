import os
import argparse
import logging

from PIL import Image

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Thumbnailer(object):
    preview_dirname = 'previews'
    SIZES = [(".l", 3000),
             (".m", 2000),
             ("", 1280),
             (".s", 800),
             (".xs", 600),
             ]

    def __init__(self, directory, books=False):
        self.directory = directory
        if books:
            self.SIZES = [('', 500)]
            self.preview_dirname = 'books'

        self.preview_dirpath = os.path.join(directory, self.preview_dirname)

        if not os.path.exists(self.preview_dirpath):
            os.makedirs(self.preview_dirpath)

    def process_files(self, files):
        for f in files:
            if not f.endswith(('jpeg', 'jpg', 'png', 'webp')):
                continue
            self.create_thumbnails(f)

    def create_thumbnails(self, f):
        filepath = os.path.join(self.directory, f)
        logger.info("Processing %s", f)
        with Image.open(filepath) as im:
            im = im.convert('RGB')
            for suffix, size in self.SIZES:
                filename, ext = os.path.splitext(f)
                new_name = filename + suffix + '.jpeg'
                logger.info("Image %s, size %s", f, size)
                previewpath = os.path.join(self.preview_dirpath, new_name)
                if os.path.exists(previewpath):
                    continue
                im.thumbnail((size, size))
                im.save(previewpath, "JPEG", optimize=True, quality=95)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input_dir', action='store', dest='input_dir', required=True)
    parser.add_argument('-b', '--books', action='store_true')
    return parser.parse_args()


def main():
    args = parse_args()

    dirpath, dirnames, filenames = next(os.walk(args.input_dir))
    t = Thumbnailer(args.input_dir, args.books)
    t.process_files(filenames)


if __name__ == '__main__':
    main()
