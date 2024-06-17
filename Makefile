build:
	docker build -t env_designpattern .
run:
	docker run --name env_designpattern -it -v .:/src env_designpattern
