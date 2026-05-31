#!/bin/bash

set -e

PROJECT_ROOT="$(git rev-parse --show-toplevel)"
cd "$PROJECT_ROOT"

echo "Deploying Loki..."

kubectl apply -R -f infrastructure/monitoring/loki

kubectl rollout status deployment/loki -n logging

echo "Loki deployed successfully."