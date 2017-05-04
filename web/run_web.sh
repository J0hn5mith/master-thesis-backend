#!/bin/bash

sleep 10

./manage.py syncdb
./manage.py migrate
/usr/local/bin/gunicorn master_thesis_backend.wsgi:application -w 2 -b :8000 --access-logfile ./access_log.log
