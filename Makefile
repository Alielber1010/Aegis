.PHONY: up down test lint eval

up:
	docker compose up -d --build

down:
	docker compose down

test:
	pytest

lint:
	ruff check src tests evals

eval:
	python -m evals.run evals/experiments/$(EXP).yaml
