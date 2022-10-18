import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portfolio_site.settings")
app = Celery("portfolio_site")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
