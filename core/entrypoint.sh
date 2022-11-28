#!/bin/sh
export DJANGO_SUPERUSER_PASSWORD=123456

python3 manage.py collectstatic --noinput
python3 manage.py migrate
python3 manage.py loaddata access_levels
python3 manage.py createsuperuser --user sepehr --noinput
pyhton3 manage.py runserver 0.0.0.0:8000

exec "$@"