import os
from celery import Celery

# For Heroku deploy
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_trushevych.settings')
#
# BASE_REDIS_URL = os.environ.get('REDIS_URL', 'redis://localhost:6379')
#
# app = Celery('django_trushevych', backend='rpc://', broker='pyamqp://')
#
# app.config_from_object('django.conf:settings', namespace='CELERY')
#
# app.autodiscover_tasks()
#
# app.conf.broker_url = BASE_REDIS_URL
# app.conf.beat_scheduler = 'django_celery_beat.schedulers.DatabaseScheduler'


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_trushevych.settings')

app = Celery('django_trushevych')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
