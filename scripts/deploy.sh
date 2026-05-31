#!/bin/bash

set -e

PROJECT_ROOT="$(git rev-parse --show-toplevel)"
cd "$PROJECT_ROOT"

./scripts/build-images.sh

./scripts/load-images.sh

./scripts/create-secrets.sh

./scripts/deploy-k8s.sh

echo "SentinelAI fully deployed."