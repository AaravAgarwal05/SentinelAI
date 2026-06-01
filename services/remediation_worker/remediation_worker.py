import json
import pika

from shared.logger import get_logger
from shared.models.remediation import RemediationRequest
from shared.rabbitmq_client import create_connection
from shared.config import (
    get_env,
    get_env_int
)

EXCHANGE_NAME = get_env("EXCHANGE_NAME")
REMEDIATION_QUEUE = get_env("REMEDIATION_QUEUE")
REMEDIATION_ROUTING_KEY = get_env("REMEDIATION_ROUTING_KEY")

logger = get_logger(__name__)

logger.info("Starting SentinelAI Remediation Worker...")

connection = create_connection()

channel = connection.channel()

channel.exchange_declare(
    exchange=EXCHANGE_NAME,
    exchange_type='topic',
    durable=True
)

channel.queue_declare(
    queue=REMEDIATION_QUEUE,
    durable=True
)

channel.queue_bind(
    exchange=EXCHANGE_NAME,
    queue=REMEDIATION_QUEUE,
    routing_key=REMEDIATION_ROUTING_KEY
)

channel.basic_qos(prefetch_count=1)

def callback(ch, method, properties, body):

    try:

        remediation_request = RemediationRequest(
            **json.loads(body.decode())
        )

        logger.warning(
            f"DRY RUN | "
            f"action={remediation_request.action} "
            f"service={remediation_request.service} "
        )

        logger.info(
            f"reason={remediation_request.reason} "
        )

        ch.basic_ack(delivery_tag=method.delivery_tag)

    except Exception as e:

        logger.exception(
            f"Failed remediation incident: {e}"
        )

        ch.basic_nack(
            delivery_tag=method.delivery_tag,
            requeue=False
        )

channel.basic_consume(
    queue=REMEDIATION_QUEUE,
    on_message_callback=callback
)

logger.info("Waiting for remediation requests...")

channel.start_consuming()