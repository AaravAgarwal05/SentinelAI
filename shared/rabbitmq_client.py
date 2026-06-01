import pika
import time 

from shared.config import (
    get_env,
    get_env_int
)
from shared.logger import get_logger

logger = get_logger(__name__)

RABBITMQ_HOST = get_env("RABBITMQ_HOST")
RABBITMQ_PORT = get_env_int("RABBITMQ_PORT")
RABBITMQ_USERNAME = get_env("RABBITMQ_USERNAME")
RABBITMQ_PASSWORD = get_env("RABBITMQ_PASSWORD")

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
