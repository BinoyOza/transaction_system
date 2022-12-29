# django_celery/celery.py

import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "transaction_system.settings")
app = Celery("transaction_system")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.conf.update(
    task_routes={
        'customers.tasks.customers_task': {'queue': 'customers'},
        'orders.tasks.orders_task': {'queue': 'orders'}
    },
)
app.autodiscover_tasks()
