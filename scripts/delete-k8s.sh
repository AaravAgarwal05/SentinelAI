#!/bin/bash

set -e

echo "Deleting Kubernetes resources..."

kubectl delete -R -f kubernetes/

echo "Cleanup completed."
