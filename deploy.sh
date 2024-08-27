#!/bin/bash

set -e

IMAGE_NAME="your-repo-name/fastapi-app"
REGISTRY_URL="registry.vultr.com"
SHA=$(git rev-parse --short HEAD) # Get the short SHA of the current commit

# Build the Docker image
docker build -t "${IMAGE_NAME}":"${SHA}" .

# Tag the Docker image with SHA and push it to Vultr container registry
docker tag ${IMAGE_NAME}:"${SHA}" ${REGISTRY_URL}/${IMAGE_NAME}:"${SHA}"
docker push ${REGISTRY_URL}/${IMAGE_NAME}:"${SHA}"

docker-compose up -d
