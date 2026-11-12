#!/bin/sh
set -e

if [ "$DJANGO_ENV" = "development" ]; then
    echo "Running Development Server"
    # In dev, we just need to make sure the database is up-to-date
    python manage.py migrate
    python manage.py ensure_superuser
    exec python manage.py runserver 0.0.0.0:8000
else
    echo "Running Production Server"
    # In prod, we just need to make sure the database is up-to-date
    python manage.py migrate
    python manage.py ensure_superuser
    exec gunicorn mysite.wsgi:application --bind 0.0.0.0:8000
fi