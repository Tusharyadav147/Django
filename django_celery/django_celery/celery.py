from __future__ import absolute_import, unicode_literals
import os
from celery.schedules import crontab

from celery import Celery
from django.conf import settings 


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_celery.settings")
app = Celery("django_celery")
app.conf.enable_utc = False

# celery beat settings
app.conf.beat_schedule = {
    "send_mail_every_day_at_8":{
        "task": "mainapp.tasks.send_email_func",
        "schedule": crontab(hour = 15, minute = 46),
        # "args": (2,)
    }
}

app.conf.update(timezone = "Asia/kolkata")

app.config_from_object(settings, namespace="CELERY")

app.autodiscover_tasks()

@app.task(bind = True)
def debug_task(self):
    print(f"Request: {self.request!r}")


# run celery using command ;- celery -A django_celery.celery worker --pool=solo -l info
# run celery beat using command :- celery -A django_celery beat -l INFO

