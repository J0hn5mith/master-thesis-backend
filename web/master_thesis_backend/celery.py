import os
from celery import Celery
from master_thesis_backend import load_env

load_env.load_env(True)

# set the default Django settings module for the 'celery' program.
# os.environ.setdefault(
# 'DJANGO_SETTINGS_MODULE',
# # TODO: automatically use right one!
# 'master_thesis_backend.settings.dev'
# )
app = Celery('master_thesis_backend')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
