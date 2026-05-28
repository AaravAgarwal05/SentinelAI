#!/bin/bash

set -e

echo "Deleting Kubernetes resources..."

kubectl delete -f kubernetes/

echo "Cleanup completed."