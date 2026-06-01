#!/bin/bash

set -e

echo "Loading sentinel-api into Kind..."

kind load docker-image sentinel-api --name sentinel

echo "Loading sentinel-incident-worker into Kind..."

kind load docker-image sentinel-incident-worker --name sentinel

echo "Loading sentinel-remediation-worker into Kind..."

kind load docker-image sentinel-remediation-worker --name sentinel

echo "All images loaded successfully."