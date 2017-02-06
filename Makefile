.PHONY: test
test:
	docker build -t avro-testing-image .

.PHONY: test-py
test-py:
	make -C lang/py test
