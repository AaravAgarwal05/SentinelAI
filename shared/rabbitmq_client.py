import pika
import time 

from shared.config import (
    RABBITMQ_HOST,
    RABBITMQ_PORT,
    RABBITMQ_USERNAME,
    RABBITMQ_PASSWORD
)

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

            print("Connected to RabbitMQ")

            return connection

        except pika.exceptions.AMQPConnectionError:

            print("RabbitMQ not ready, retrying in 5 seconds...")

            time.sleep(5)
