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
