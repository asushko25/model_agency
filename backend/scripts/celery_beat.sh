#!/bin/sh

echo "Starting Celery Worker"

celery -A model_agency worker -l info
