# django-orm-mastery
```
python -m venv .venv   

source .venv/bin/activate  

```
pypi 
```
pip install
pip uninstall
pip list
pip freeze


pip install Django==4.1.1        
python -m pip install --upgrade pip

pip freeze > requirements.txt
```


Create a new Django project
```
django-admin startproject core .
```
In this experiemnt core is the name of the project
with . creates the core folder in the root folder
without it creates a folder named core and another core folder inside it


pip install python-decouple 

settings.py
from decouple import config

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG')

- Create a new app inside core folder
mkdir ./core/newapp                      
./manage.py startapp newapp ./core/newapp

- After create an app it is necessary to register the application in settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'newapp',
]




