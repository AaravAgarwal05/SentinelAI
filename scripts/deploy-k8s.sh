#!/bin/bash

set -e

echo "Deploying Kubernetes manifests..."

kubectl apply -R -f kubernetes/

echo "Deployment completed."