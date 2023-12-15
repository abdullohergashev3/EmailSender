# celerybeat.conf

[celerybeat]
schedule = celery.schedules:timedelta(seconds=20)


# celery -A celery_app beat --loglevel=info -s celerybeat.scheduler:DatabaseScheduler -s djcelery.scheduler.DatabaseScheduler --detach 1 -l INFO