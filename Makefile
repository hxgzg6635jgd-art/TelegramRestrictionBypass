.PHONY: help install install-dev clean lint format test run docker-build docker-up docker-down

help:  ## Show this help message
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Available targets:'
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'

install:  ## Install production dependencies
	pip install -r requirements.txt

install-dev:  ## Install development dependencies
	pip install -r requirements.txt -r requirements-dev.txt

clean:  ## Clean up temporary files and caches
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	rm -rf .pytest_cache .coverage htmlcov

lint:  ## Run code linters
	@echo "Running flake8..."
	flake8 . || true
	@echo "Running pylint..."
	pylint main.py config.py logger.py helpers/ || true

format:  ## Format code with black and isort
	@echo "Running black..."
	black .
	@echo "Running isort..."
	isort .

test:  ## Run tests (when available)
	pytest -v

run:  ## Run the bot
	python main.py

docker-build:  ## Build Docker image
	docker compose build

docker-up:  ## Start bot in Docker
	docker compose up -d

docker-down:  ## Stop Docker containers
	docker compose down

docker-logs:  ## View Docker logs
	docker compose logs -f
