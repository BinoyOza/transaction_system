import structlog

from transaction_system.celery import app

logging = structlog.get_logger(__name__)


@app.task
def customers_task():
    print("This is the customers task.")
    logging.info("This is the customers task.")
