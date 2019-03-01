.PHONY: all
all: test

.PHONY: install-hooks
install-hooks:
	tox -e pre-commit -- install -f --install-hooks

.PHONY: test
test:
	tox

.PHONY: tests
tests: test

.PHONY: acceptance
acceptance:
	tox -e acceptance

.PHONY: clean
clean:
	rm -rf .tox build dist *.egg-info
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -delete
	find . -name '*.jar' -delete

.PHONY: update-protobuf
update-protobuf:
	$(MAKE) -C py_zipkin/encoding/protobuf update-protobuf
