#!/bin/sh

echo "Migrating database files..."

python manage.py migrate --noinput

echo "Starting Gunicorn server..."
ginicorn model_agency.wsgi:application --bind 0.0.0.0:$PORT
