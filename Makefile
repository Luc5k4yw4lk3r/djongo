RUN=docker-compose run --rm DjangoMongoSRL

build:
	docker-compose build

run:
	docker-compose up

shell:
	sudo docker exec -t -i djongo_djongo_1  bash

test:
	$(RUN) pytest -x -vvv --pdb

stop:
	docker-compose down