default: 
	@echo "Comandos disponíveis "
	@echo "	make build           - cria containers caso não os tenha, ou caso modifique .env.dev"
	@echo "	make makemigrations  - cria migrations"
	@echo "	make migrate         - executa migrations"
	@echo "	make createsuperuser - criar um usuario"
	@echo "	make start           - inicializa container, e executa serviço Django"
	@echo "	make stop            - encerra execução dos containers BD e Django"

build:
	docker-compose -f docker-compose-dev.yaml up -d --build --remove-orphans

makemigrations:
	docker exec -ti boiler_plate_web_dev python manage.py makemigrations

migrate:
	docker exec -ti boiler_plate_web_dev python manage.py migrate

createsuperuser:
	docker exec -ti boiler_plate_web_dev python manage.py createsuperuser

start:
	docker-compose -f docker-compose-dev.yaml start
	docker exec -ti boiler_plate_web_dev python manage.py runserver 0.0.0.0:8000

stop:
	docker-compose -f docker-compose-dev.yaml stop 


