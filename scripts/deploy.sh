#!/bin/bash

set -e

cd "$(dirname "$0")/.."

./scripts/build-images.sh

./scripts/load-images.sh

./scripts/create-secrets.sh

./scripts/deploy-k8s.sh

echo "SentinelAI fully deployed."