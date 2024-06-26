#!/bin/bash


DIR=$1

if [[ -z $DIR ]];
then
    echo "Missing directory argument!"
    exit 1
fi

python scripts/exif_order.py -i $DIR
python scripts/resize_photos.py -i $DIR
/Applications/ImageOptim.app/Contents/MacOS/ImageOptim $DIR*
python scripts/upload_to_s3.py -i $DIR --no-dryrun
python scripts/add_photos.py -i $DIR
exit 0