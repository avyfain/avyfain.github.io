#!/bin/bash

osascript get_urls.scpt
TODAY=`date '+%Y-%m-%d'`;
FNAME="_posts/links/$TODAY-links.md"
pbpaste > $FNAME
echo $FNAME