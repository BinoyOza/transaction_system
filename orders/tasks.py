from celery.utils.log import get_task_logger

from transaction_system.celery import app


logging = get_task_logger(__name__)


@app.task
def orders_task():
    print("This is the orders task.")
    logging.info("This is the orders task.")
    return
