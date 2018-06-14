#!/bin/bash


DIR=$1

if [[ -z $DIR ]];
then
    echo "Missing directory argument!"
    exit 1
fi

python scripts/resize_photos.py -i $DIR
python scripts/upload_to_s3.py -i $DIR --no-dryrun
python scripts/add_photos.py -i $DIR