#!/bin/bash

set -e

echo "Building sentinel-api image..."

docker build -t sentinel-api \
-f services/api_service/Dockerfile .

echo "Building sentinel-incident-worker image..."

docker build -t sentinel-incident-worker \
-f services/incident_worker/Dockerfile .

docker build -t sentinel-remediation-worker \
-f services/remediation_worker/Dockerfile .

echo "All images built successfully."