update-protobuf:
	curl -L https://raw.githubusercontent.com/openzipkin/zipkin-api/master/zipkin.proto > zipkin.proto
	protoc --python_out=. --mypy_out=. zipkin.proto
