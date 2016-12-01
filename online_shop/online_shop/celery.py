import os

from celery import Celery
from django.conf import settings

# Основыне настройки Django для celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'online_shop.settings')

app = Celery('online_shop')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
