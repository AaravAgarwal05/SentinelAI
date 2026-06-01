import time
import json
import pika

from shared.logger import get_logger
from shared.models.incident import Incident
from shared.models.remediation import RemediationRequest
from shared.rabbitmq_client import create_connection
from shared.config import (
    get_env,
    get_env_int
)

EXCHANGE_NAME = get_env("EXCHANGE_NAME")
INCIDENT_QUEUE = get_env("INCIDENT_QUEUE")
INCIDENT_ROUTING_KEY = get_env("INCIDENT_ROUTING_KEY")
REMEDIATION_ROUTING_KEY = get_env("REMEDIATION_ROUTING_KEY")

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
    routing_key=INCIDENT_ROUTING_KEY
)

channel.basic_qos(prefetch_count=1)

def callback(ch, method, properties, body):

    try:

        incident = Incident(
            **json.loads(body.decode())
        )

        logger.info(
            f"Received incident | "
            f"service={incident.service} "
            f"severity={incident.severity} "
            f"event_type={incident.event_type}"
        )

        remediation = None

        if incident.event_type == "crash":

            remediation = RemediationRequest(
                service=incident.service,
                namespace=incident.namespace,
                action="restart-deployment",
                reason="Service crash detected"
            )

        if remediation:

            channel.basic_publish(
                exchange=EXCHANGE_NAME,
                routing_key=REMEDIATION_ROUTING_KEY,
                body=remediation.model_dump_json(),
                properties=pika.BasicProperties(
                    delivery_mode=2
                )
            )

            logger.info(
                f"Published remediation request | "
                f"action={remediation.action}"
            )

        ch.basic_ack(
            delivery_tag=method.delivery_tag
        )

    except Exception as e:

        logger.exception(
            f"Failed processing incident: {e}"
        )

        ch.basic_nack(
            delivery_tag=method.delivery_tag,
            requeue=False
        )

channel.basic_consume(
    queue=INCIDENT_QUEUE,
    on_message_callback=callback
)

logger.info("Waiting for incidents...")

channel.start_consuming()
