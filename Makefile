.PHONY: up build stop down restart rebuild destroy destroy-volumes ps logs app amend fmt run

up:
	docker compose up -d

build:
	docker compose build --no-cache --force-rm

stop:
	docker compose stop

down:
	docker compose down --remove-orphans

restart:
	@make down
	@make up

rebuild:
	@make down
	@make build
	@make up

destroy:
	docker compose down --rmi all --volumes --remove-orphans

destroy-volumes:
	docker compose down --volumes --remove-orphans

ps:
	docker compose ps

logs:
	docker compose logs -f

app:
	docker compose exec app bash

amend:
	git commit --amend

fmt:
	docker compose exec app bash -c 'black .'

run:
	docker compose exec app bash -c 'python /app/src/main.py'
test:
	docker compose exec app bash -c 'python -m pytest -s'