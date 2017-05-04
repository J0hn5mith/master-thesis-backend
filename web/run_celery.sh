#!/bin/sh
#https://blog.syncano.io/configuring-running-django-celery-docker-containers-pt-1/

# wait for RabbitMQ server to start
sleep 10

# run Celery worker for our project myproject with Celery configuration stored in Celeryconf
#su -m myuser -c "celery worker -A master_thesis_backend.celery -Q default -n default@%h"  

celery worker -A master_thesis_backend --loglevel=info
