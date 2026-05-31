#!/bin/bash

set -e

echo "Starting SentinelAI bootstrap..."

./scripts/create-namespaces.sh

./scripts/infrastructure/deploy-rabbitmq.sh

echo "Bootstrap completed."
