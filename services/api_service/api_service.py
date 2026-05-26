from fastapi import FastAPI
from fastapi.responses import Response

from prometheus_client import (
    Counter,
    generate_latest
)

import pika

from shared.rabbitmq_client import create_connection

from shared.config import (
    EXCHANGE_NAME,
    INCIDENT_ROUTING_KEY
)

from shared.models import Incident

app = FastAPI()

incident_counter = Counter(
    'sentinel_incidents_total',
    'Total incidents received'
)

@app.get("/")
def health():

    return {
        "status": "SentinelAI API running"
    }

@app.post("/incident")
def create_incident(incident: Incident):

    incident_counter.inc()

    connection = create_connection()

    channel = connection.channel()

    channel.exchange_declare(
        exchange=EXCHANGE_NAME,
        exchange_type='topic',
        durable=True
    )

    channel.basic_publish(
        exchange=EXCHANGE_NAME,
        routing_key=INCIDENT_ROUTING_KEY,
        body=incident.model_dump_json(),
        properties=pika.BasicProperties(
            delivery_mode=2
        )
    )

    connection.close()

    return {
        "status": "incident published",
        "incident": incident
    }

@app.get("/metrics")
def metrics():

    return Response(
        generate_latest(),
        media_type="text/plain"
    )
