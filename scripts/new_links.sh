#!/bin/bash

osascript get_urls.scpt
TODAY=`date '+%Y-%m-%d'`;
YEAR=`date +"%Y"`
FNAME="_posts/links/$YEAR/$TODAY-links.md"
pbpaste > $FNAME
echo $FNAME