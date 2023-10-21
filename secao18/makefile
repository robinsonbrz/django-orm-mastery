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


recreatedb:
	# @echo "Cleaning up migration files in accounts, companies, and customers..."
	# find accounts/migrations/ -type f ! -name '__init__.py' -delete
	# find companies/migrations/ -type f ! -name '__init__.py' -delete
	# find customers/migrations/ -type f ! -name '__init__.py' -delete
	# @echo "Migration files cleanup completed."
	docker exec -ti boiler_plate_db_dev psql -h localhost -U postgres password=postgres -c  "SELECT \
	pg_terminate_backend(pg_stat_activity.pid) \
	FROM pg_stat_activity WHERE pg_stat_activity.datname = 'ingresso_express' \
	AND pid <> pg_backend_pid();"
	@echo "##################_____________________________________ DB unlocked"
	docker exec -ti boiler_plate_db_dev psql -h localhost -U postgres password=postgres -c 'DROP DATABASE ingresso_express;'
	docker exec -ti boiler_plate_db_dev psql -h localhost -U postgres password=postgres -c '\l+'
	docker exec -ti boiler_plate_db_dev psql -h localhost -U postgres password=postgres -c 'CREATE DATABASE ingresso_express;'
	docker exec -ti boiler_plate_db_dev psql -h localhost -U postgres password=postgres -c '\l+'
	@echo "##################_____________Recreation of the Database completed."
	docker exec -ti web_ingresso_dev python manage.py makemigrations
	docker exec -ti web_ingresso_dev python manage.py migrate