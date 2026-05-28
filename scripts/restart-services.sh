#!/bin/bash

set -e

echo "Restarting API deployment..."

kubectl rollout restart deployment sentinel-api

echo "Restarting incident worker deployment..."

kubectl rollout restart deployment sentinel-worker

echo "Restarting remediation worker deployment..."

kubectl rollout restart deployment remediation-worker

echo "All services restarted."