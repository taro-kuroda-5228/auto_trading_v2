include envs/.env
export

run:
	docker run --detach -it --rm \
	-p $(IP_HOST):$(PORT_HOST):$(PORT_CONTAINER) \
	-v /mnt/c/Users/User/$(DIRECTORY_NAME):/home/work \
	--name $(CONTAINER_NAME) \
	$(IMAGE_NAME):$(TAG_NAME) \
	/bin/bash
jl:
	docker exec -it \
	$(CONTAINER_NAME) \
	jupyter lab \
	--port $(PORT_CONTAINER) --ip="0.0.0.0" \
	--allow-root \
	--NotebookApp.token='' \
	--no-browser
stop:
	docker stop $(CONTAINER_NAME)
