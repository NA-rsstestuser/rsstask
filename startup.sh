#!/bin/sh
export DJANGO_SUPERUSER_EMAIL=admin@ikn.net
export DJANGO_SUPERUSER_PASSWORD=admin
python manage.py migrate
python manage.py createsuperuser --username=admin --no-input
python manage.py runserver 0.0.0.0:8000