#!/bin/sh

echo "Starting Celery Beat"

celery -A model_agency beat -l info
