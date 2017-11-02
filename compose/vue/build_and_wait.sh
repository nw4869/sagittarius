#!/bin/bash
DIST_DIR=/app/dist

rm -rf DIST_DIR/*

cnpm install && npm run build && echo 'build done.' && touch $DIST_DIR/__BUILD_DONE__

# while [ "$(ls -A DIST_DIR)" ] ;
# do
# 	echo Waiting for files to be moved.
#     sleep 2
# done
#
# echo 'all done.'
