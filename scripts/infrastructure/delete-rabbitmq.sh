#!/bin/bash

set -e

PROJECT_ROOT="$(git rev-parse --show-toplevel)"
cd "$PROJECT_ROOT"

echo "Deleting RabbitMQ..."

kubectl delete -R -f "./infrastructure/messaging/rabbitmq" --ignore-not-found=true

echo "RabbitMQ deleted successfully."