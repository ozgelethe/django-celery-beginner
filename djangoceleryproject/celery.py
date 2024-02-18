from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from django.conf import settings
from celery.schedules import crontab
# from django_celery_beat.models import PeriodicTask

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoceleryproject.settings')

app = Celery('djangoceleryproject')

app.conf.update(timezone='Europe/Istanbul')

broker_connection_retry_on_startup = True

app.conf.update(timezon = 'Europe/Istanbul')

app.config_from_object(settings, namespace='CELERY')


# Celery Beat Settings

app.conf.beat_schedule = {
    'send-mail-everyday-at-8' : {
        'task' : 'mail.tasks.send_mail_func',
        'schedule' : crontab(hour=23, minute=6),
        # Celery Schedules - https://docs.celeryproject.org/en/stable/reference/celery.schedules.html
        #'args' : (2,)
    }
}

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')