#!/bin/bash

set -e

echo "Loading sentinel-api into Kind..."

kind load docker-image sentinel-api --name sentinel

echo "Loading sentinel-worker into Kind..."

kind load docker-image sentinel-worker --name sentinel

echo "All images loaded successfully."