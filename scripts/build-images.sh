#!/bin/bash

set -e

echo "Building sentinel-api image..."

docker build -t sentinel-api \
-f services/api_service/Dockerfile .

echo "Building sentinel-worker image..."

docker build -t sentinel-worker \
-f services/incident_worker/Dockerfile .

echo "All images built successfully."