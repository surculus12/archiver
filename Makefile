IMAGE_TAG := archiver

build:
	docker build -t $(IMAGE_TAG) .

run: build
	docker run --rm $(IMAGE_TAG) -v ./data:/data
