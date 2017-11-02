#!/bin/sh

# waiting for frontend static file to build
DIST_DIR_BUILD_DONE_FLAG=/app/frontend/dist/__BUILD_DONE__
while [ ! -f $DIST_DIR_BUILD_DONE_FLAG ] ;
do
	echo waiting for frontend static file to build
    sleep 3
done

python /app/manage.py collectstatic --noinput
/usr/local/bin/gunicorn config.wsgi -w 4 -b 0.0.0.0:5000 --chdir=/app
