
.PHONY: *

# [start]
ROOT_DIR:=$(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))

IMAGE_TAG_VERSION=220507-0
ENV_PREFIX=IMAGE_TAG_VERSION=$(IMAGE_TAG_VERSION)
OPTION=--file=./docker/docker-compose.yaml

build:
	$(ENV_PREFIX) docker-compose $(OPTION) build

RUN_SERVICE_NAME=main

start:
	PORT=8080 HMAC_SECRET=test_secret go run ./main.go

start.docker:
	$(ENV_PREFIX) docker-compose $(OPTION) run --rm --service-ports $(RUN_SERVICE_NAME)
debug:
	$(ENV_PREFIX) docker-compose $(OPTION) run --rm --entrypoint=bash --service-ports $(RUN_SERVICE_NAME)

down:
	$(ENV_PREFIX) docker-compose $(OPTION) down

reset:
	$(ENV_PREFIX) docker-compose $(OPTION) down --volumes

push:
	$(ENV_PREFIX) docker-compose $(OPTION) push

run:
	$(ENV_PREFIX) docker-compose $(OPTION) run --service-ports $(RUN_SERVICE_NAME)