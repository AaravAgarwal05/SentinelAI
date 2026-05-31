import pika
import time 

from shared.config import (
    RABBITMQ_HOST,
    RABBITMQ_PORT,
    RABBITMQ_USERNAME,
    RABBITMQ_PASSWORD
)
from shared.logger import get_logger

logger = get_logger(__name__)

def create_connection():

    credentials = pika.PlainCredentials(
        RABBITMQ_USERNAME,
        RABBITMQ_PASSWORD
    )

    parameters = pika.ConnectionParameters(
        host=RABBITMQ_HOST,
        port=RABBITMQ_PORT,
        credentials=credentials
    )

    while True:

        try:
            connection = pika.BlockingConnection(parameters)

            logger.info("Connected to RabbitMQ")

            return connection

        except pika.exceptions.AMQPConnectionError:

            logger.warning("RabbitMQ not ready, retrying in 5 seconds...")

            time.sleep(5)
