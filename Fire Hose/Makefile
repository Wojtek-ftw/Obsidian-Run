.PHONY: build up down logs clean

build:
	docker-compose build

up:
	docker-compose up

down:
	docker-compose down

logs:
	docker-compose logs -f

clean: down
	docker system prune -f
	rm -f processor/output.csv
