#!/bin/sh

until nc -z $POSTGRES_HOST $POSTGRES_PORT; do
    sleep 1
done

python manage.py migrate

gunicorn settings.wsgi:application --bind 0.0.0.0:8000