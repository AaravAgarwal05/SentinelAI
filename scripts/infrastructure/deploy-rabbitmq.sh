#!/bin/bash

set -e

PROJECT_ROOT="$(git rev-parse --show-toplevel)"
cd "$PROJECT_ROOT"

echo "Developing RabbitMQ Secret..."

./scripts/infrastructure/create-rabbitmq-secret.sh

echo "Deploying RabbitMQ..."

kubectl apply -R -f "./infrastructure/messaging/rabbitmq"

echo "RabbitMQ deployed successfully."