import os

from celery import Celery
from celery.schedules import crontab

import vessel.tasks


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

app = Celery('boats')
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
app.conf.update(
    timezone='UTC',
    enable_utc=True,
)
app.conf.beat_schedule = {
    'load_vessels_movements_file_everyday': {
        'task': 'vessel.tasks.load_vessels_movements_file',
        'schedule': crontab(hour=0, minute=0),
    },
}
