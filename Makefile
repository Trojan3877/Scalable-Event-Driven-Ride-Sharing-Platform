up:
	docker-compose up --build

down:
	docker-compose down

logs:
	docker-compose logs -f

test:
	pytest --cov=services tests/