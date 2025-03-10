#!/bin/sh

echo "Migrating database files..."

python manage.py migrate --noinput

echo "Installing static data of 24 models"
python manage.py loaddata seed_data/fixture_db_data.json

echo "Starting Gunicorn server..."
gunicorn model_agency.wsgi:application --bind 0.0.0.0:$PORT
