#!/bin/bash
DIST_DIR=/app/dist
DIST_DIR_SHARED=/app/dist_shared

rm -rf $DIST_DIR_SHARED/*

cp -R $DIST_DIR/* $DIST_DIR_SHARED && touch $DIST_DIR_SHARED/__BUILD_DONE__

