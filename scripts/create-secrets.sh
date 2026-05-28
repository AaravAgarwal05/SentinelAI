#!/bin/bash

set -e

echo "Deleting old secret if exists..."

kubectl delete secret sentinel-env --ignore-not-found

echo "Creating new secret from .env.k8s..."

kubectl create secret generic sentinel-env \
--from-env-file=.env.k8s

echo "Secret created successfully."