all:
	@echo "NO CAPES, eh no defaults!"

# run without debug
run:
	cd app &&\
	python manage.py runserver

# Make migration
mm:
	cd app &&\
	python manage.py makemigrations

# Migrate
m:
	cd app &&\
	python manage.py migrate

# Make requirements.txt
mr:
	poetry export -f requirements.txt --output requirements.txt --without-hashes

# Run celery worker
run-worker:
	cd app &&\
	poetry run celery -A app worker -l INFO -E

# Run celery scheduler
run-beat:
	cd app &&\
	poetry run celery -A app beat -l INFO

# Create superuser
su:
	cd app &&\
	python manage.py createsuperuser

# Config git so that it doesn't complain about file permissions
config-git:
	git config --global --add safe.directory /workspace
	git config core.fileMode false

# Make requirements.txt
req:
	poetry export -f requirements.txt --output requirements.txt --without-hashes

# Build, run docker
docker: req docker-build docker-run

docker-build:
	docker build -t django-devcontainer .

docker-run:
	docker run --rm --env-file .env.local -p 8080:8000 django-devcontainer
