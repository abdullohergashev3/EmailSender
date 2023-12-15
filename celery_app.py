from celery import Celery

from

celery = Celery(
    'main',
    brokes='redis://localhost:6379/0',
    backend='redis://localhost:6379/0'
)


@celery.task
def send_email():
    emails = get_emails()
    for email in emails:
        pass
