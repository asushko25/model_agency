import os

import celery

from django.conf import settings

from datetime import timedelta


os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "model_agency.settings"
)
# celery -A model_agency worker
celery_app = celery.Celery("model_agency")
celery_app.config_from_object(settings, namespace="CELERY")


# plan to run specific task every num of days in
# settings.CELERY_CHECK_NEWSLETTERS
celery_app.conf.beat_schedule.update({
    "checking_newsletters_subscribers": {
        "task": "newsletter.tasks.send_emails_to_newsletter_subscribers",
        "schedule": timedelta(
            days=settings.CELERY_CHECK_NEWSLETTERS
        )
    }
})

celery_app.conf.update(
    timezone="UTC",
    # set higher maximum interval for beat checks
    beat_max_loop_interval=(
        settings.CELERY_MAX_BEAT_INTERVAL_SECONDS
    ),
    broker_connection_retry_on_startup=True
)

celery_app.autodiscover_tasks()
