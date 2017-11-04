#!/bin/bash
DIST_DIR=/app/dist

rm -rf DIST_DIR/*

npm install && npm run build && echo 'build done.' && touch $DIST_DIR/__BUILD_DONE__
