web: gunicorn django_trushevych.wsgi:application --log-file -
worker: celery -A django_dontsov worker --beat --concurrency 10 -l info
