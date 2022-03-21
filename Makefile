build:
	@docker build -t boats-app .
up:
	@docker-compose run app python manage.py migrate
	@docker-compose up -d
createadmin:
	@docker-compose run app python manage.py createsuperuser