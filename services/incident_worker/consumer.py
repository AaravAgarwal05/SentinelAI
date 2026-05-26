import time
import json

from shared.models import Incident
from shared.rabbitmq_client import create_connection
from shared.config import (
    EXCHANGE_NAME,
    INCIDENT_QUEUE
)

print("Starting SentinelAI Incident Worker...")

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

    print("\n========== INCIDENT RECEIVED ==========")

    print(f"Service: {incident.service}")

    print(f"Severity: {incident.severity}")

    print(f"Event Type: {incident.event_type}")

    print(f"Namespace: {incident.namespace}")

    print(f"Message: {incident.message}")

    print(f"Timestamp: {incident.timestamp}")

    time.sleep(3)

    print("Incident processed")

    ch.basic_ack(
        delivery_tag=method.delivery_tag
    )

channel.basic_consume(
    queue=INCIDENT_QUEUE,
    on_message_callback=callback
)

print("Worker listening for incidents...")

channel.start_consuming()
