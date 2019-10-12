TARGZ_FILE := amazon-kinesis-firehose-for-fluent-bit.tar.gz
IMAGE_NAME := amazon-kinesis-firehose-for-fluent-bit-package
amazonlinux2: IMAGE_NAME := $(IMAGE_NAME)-amazonlinux2

.PHONY: all clean amazonlinux2 bintray

all: amazonlinux2
amazonlinux2: amazonlinux2.build

%.build: Dockerfile.% rpmbuild/SPECS/amazon-kinesis-firehose-for-fluent-bit.spec
	[ -d $@.bak ] && rm -rf $@.bak || :
	[ -d $@ ] && mv $@ $@.bak || :
	tar -czf - Dockerfile.$* rpmbuild | docker build --file Dockerfile.$* -t $(IMAGE_NAME) -
	docker run --name $(IMAGE_NAME)-tmp $(IMAGE_NAME)
	mkdir -p tmp
	docker wait $(IMAGE_NAME)-tmp
	docker cp $(IMAGE_NAME)-tmp:/tmp/$(TARGZ_FILE) tmp
	docker rm $(IMAGE_NAME)-tmp
	mkdir $@
	tar -xzf tmp/$(TARGZ_FILE) -C $@
	rm -rf tmp Dockerfile
	docker images | grep -q $(IMAGE_NAME) && docker rmi $(IMAGE_NAME) || true

.PHONY: bintray
bintray:
	./scripts/build_bintray_json.bash \
		amazon-kinesis-firehose-for-fluent-bit

clean:
	rm -rf *.build.bak *.build bintray tmp Dockerfile
	docker images | grep -q $(IMAGE_NAME)-amazonlinux2 && docker rmi $(IMAGE_NAME)-amazonlinux2 || true
