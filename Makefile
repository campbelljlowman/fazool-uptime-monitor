REGISTRY=ghcr.io
IMAGE_NAME=campbelljlowman/fazool-uptime-uptime-monitor
STABLE_VERSION=0.1.0
UNIQUE_VERSION=${STABLE_VERSION}-${shell date "+%Y.%m.%d"}-${shell git rev-parse --short HEAD}
STABLE_IMAGE_TAG=${REGISTRY}/${IMAGE_NAME}:${STABLE_VERSION}
UNIQUE_IMAGE_TAG=${REGISTRY}/${IMAGE_NAME}:${UNIQUE_VERSION}

ENV_FILE=./.env

include .env
export

run: 
	python3 uptime_monitor.py

run-docker:
	docker run --rm \
	--env-file ${ENV_FILE} \
	-v ./destination_email_addresses.json:/app/destination_email_addresses.json \
	${UNIQUE_IMAGE_TAG}

build:
	docker build \
	-t ${STABLE_IMAGE_TAG} \
	-t ${UNIQUE_IMAGE_TAG} \
	.

publish:
	@echo ${GITHUB_ACCESS_TOKEN} | docker login ghcr.io -u campbelljlowman --password-stdin
	docker push ${UNIQUE_IMAGE_TAG}
ifeq ($(shell git rev-parse --abbrev-ref HEAD), master)
	docker push ${STABLE_IMAGE_TAG}
else 
	@echo "Not pushing stable version because not on master branch"
endif
	docker logout