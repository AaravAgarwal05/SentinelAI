#!/bin/bash

set -e

echo "Deleting old secret if exists..."

kubectl delete secret sentinel-env \
  -n sentinel \
  --ignore-not-found

echo "Creating new secret..."

cat \
  env/dev/shared.env \
  env/dev/rabbitmq.env \
  env/dev/api.env \
  env/dev/incident-worker.env \
  env/dev/remediation-worker.env \
  > /tmp/sentinel-env

kubectl create secret generic sentinel-env \
  --from-env-file=/tmp/sentinel-env \
  -n sentinel

rm /tmp/sentinel-env

echo "Secret created successfully."