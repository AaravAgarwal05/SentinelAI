#!/bin/bash

set -e

PROJECT_ROOT="$(git rev-parse --show-toplevel)"
cd "$PROJECT_ROOT"

set -a
source env/dev/rabbitmq.env
set +a

kubectl delete secret rabbitmq-secret \
  -n messaging \
  --ignore-not-found

kubectl create secret generic rabbitmq-secret \
  -n messaging \
  --from-literal=RABBITMQ_DEFAULT_USER="$RABBITMQ_USERNAME" \
  --from-literal=RABBITMQ_DEFAULT_PASS="$RABBITMQ_PASSWORD"