#!/usr/bin/env bash

python manage.py makemigrations
python manage.py migrate
#python manage.py collectstatic --noinput
uwsgi --ini docker_uwsgi.ini
