import os
import pathlib
import argparse
import logging
import multiprocessing

import boto3

from utils import retry

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

s3 = boto3.client('s3')
BUCKET = 'cdn.faingezicht.com'
IMAGE_FORMATS = ('jpeg', 'jpg', 'png')


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input_dir', action='store', dest='input_dir', required=True)
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--dryrun', dest='dryrun', action='store_true')
    group.add_argument('--no-dryrun', dest='dryrun', action='store_false')
    parser.set_defaults(dryrun=True)
    return parser.parse_args()


def file_yielder(root_path):
    parts = pathlib.Path(root_path).parts
    root = os.path.join(*parts[:-1])

    for dirpath, dirnames, filenames in os.walk(root_path):
        bucket_dir = pathlib.Path(dirpath).relative_to(root)
        for file in filenames:
            if not file.endswith(IMAGE_FORMATS):
                continue
            full_path = os.path.join(dirpath, file)
            key_id = bucket_dir.joinpath(file)
            yield full_path, str(key_id)


@retry(Exception)
def upload_file(full_path, key_id):
    logger.info("starting upload for %s", key_id)
    response = s3.upload_file(full_path, BUCKET, key_id, ExtraArgs={"ContentType": "image/jpeg"})
    logger.info("Successfully uploaded %s", key_id)
    return response


def main():
    args = parse_args()
    path = os.path.expanduser(args.input_dir)
    pool = multiprocessing.Pool(10)

    if args.dryrun:
        for path, key in file_yielder(path):
            print(path, key)
    else:
        returns = pool.starmap(upload_file, file_yielder(path))
        pool.close()
        pool.join()


if __name__ == '__main__':
    main()
