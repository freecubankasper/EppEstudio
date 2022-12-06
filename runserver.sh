#!/bin/sh
set -e

#docker run --name test1.0 -it -p 8000:8000 --network eppestudio_default -e POSTGRES_NAME=postgres -e POSTGRES_PASSWORD=postgres -e DB_USER=postgres -e DB_PASSWORD=postgres -e DB_ENGINE=django.db.backends.postgresql -e DB_NAME=postgres -e DB_HOST=db_postgres -e DB_PORT=5432 test:latest sh
cd /code
echo "Collecting Statics Files..."
python manage.py collectstatic --noinput   
echo "Starting server web..."
python manage.py runserver 0.0.0.0:8000