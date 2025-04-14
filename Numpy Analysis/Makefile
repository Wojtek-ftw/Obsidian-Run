# Name of the Docker image and container
IMAGE_NAME = my-jupyter-env
CONTAINER_NAME = jupyter-container
NOTEBOOK_PORT = 8888
NOTEBOOK_DIR = ./notebooks

.PHONY: build run stop remove logs restart

# Build the Docker image
build:
	docker build -t $(IMAGE_NAME) .

pull_image:
	docker pull $(IMAGE_NAME)

# Run the Docker container
run:
	docker run -it --rm \
		-p $(NOTEBOOK_PORT):8888 \
		-v $(NOTEBOOK_DIR):/home/jovyan/work \
		--name $(CONTAINER_NAME) \
		$(IMAGE_NAME)

# Stop and remove the container (if not using --rm)
stop:
	-docker stop $(CONTAINER_NAME)

remove:
	-docker rm $(CONTAINER_NAME)

# Show logs
logs:
	docker logs -f $(CONTAINER_NAME)

# Restart container
restart: stop run
