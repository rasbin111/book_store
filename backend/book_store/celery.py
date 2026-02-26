import os

from celery import Celery
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'book_store.settings')

app = Celery('book_store')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

app.conf.beat_schedule = {
    "delete_login_track": {
        "task": "apps.useraccount.tasks.daily_user_login_track_cleanup",
        "schedule": crontab(hour=3, minute=0), # Runs every day at 3:00 AM
    }
}