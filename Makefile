up:
	docker-compose up --build

down:
	docker-compose down

logs:
	docker-compose logs -f

test:
	pytest --cov=services tests/

lock-dev:
	pip-compile --generate-hashes requirements-dev.txt --output-file requirements-dev.lock

sync-dev:
	pip-sync requirements-dev.lock