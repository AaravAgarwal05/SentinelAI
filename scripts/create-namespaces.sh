#!/bin/bash

echo "Creating namespaces..."

kubectl apply -f namespaces/sentinel.yaml
kubectl apply -f namespaces/messaging.yaml
kubectl apply -f namespaces/monitoring.yaml
kubectl apply -f namespaces/logging.yaml

echo "Namespaces created."
