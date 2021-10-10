web: gunicorn django_trushevych.wsgi:application --log-file -
worker: celery -A tasks worker --loglevel=INFO
