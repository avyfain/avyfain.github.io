#!/bin/bash

osascript get_urls.scpt
TODAY=`date '+%Y-%m-%d'`;
pbpaste > "_posts/links/$TODAY-links.md"
