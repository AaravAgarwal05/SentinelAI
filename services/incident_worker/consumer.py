import time
import json

from shared.logger import get_logger
from shared.models import Incident
from shared.rabbitmq_client import create_connection
from shared.config import (
    EXCHANGE_NAME,
    INCIDENT_QUEUE
)

logger = get_logger(__name__)

logger.info("Starting SentinelAI Incident Worker...")

connection = create_connection()

channel = connection.channel()

channel.exchange_declare(
    exchange=EXCHANGE_NAME,
    exchange_type='topic',
    durable=True
)

channel.queue_declare(
    queue=INCIDENT_QUEUE,
    durable=True
)

channel.queue_bind(
    exchange=EXCHANGE_NAME,
    queue=INCIDENT_QUEUE,
    routing_key='infra.*.crash'
)

channel.basic_qos(prefetch_count=1)

def callback(ch, method, properties, body):

    incident_data = json.loads(body.decode())

    incident = Incident(**incident_data)

    logger.info(f"Processing incident: {incident}")

    time.sleep(2)

    logger.info(f"Finished processing incident: {incident.service}")

    ch.basic_ack(
        delivery_tag=method.delivery_tag
    )

channel.basic_consume(
    queue=INCIDENT_QUEUE,
    on_message_callback=callback
)

logger.info("Waiting for incidents...")

channel.start_consuming()
