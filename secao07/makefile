default: 
	@echo "Comandos disponíveis "
	@echo "	make install         - instala requirements"
	@echo "	make makemigrations  - cria migrations"
	@echo "	make migrate         - executa migrate"
	@echo "	make createsuperuser - criar um usuario"
	@echo "	make run             - roda servidror Django"
	@echo "	make test            - executa pytest"

	

install:
	python -m pip install --upgrade pip
	pip install -r requirements.txt

makemigrations:
	python manage.py migrate

migrate:
	python manage.py migrate

createsuperuser:
	python manage.py createsuperuser

run:
	python manage.py runserver 0.0.0.0:8000

test:
	pytest --disable-warnings -v -s


