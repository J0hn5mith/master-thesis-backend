import os
from celery import Celery
# from django.conf import settings
from master_thesis_backend import load_env

load_env.load_env()

# set the default Django settings module for the 'celery' program.
os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE',
    'master_thesis_backend.settings.dev'
)
app = Celery('master_thesis_backend')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
