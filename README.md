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

- Install project from a previous requirements file
Should activate env first
source .venv/bin/activate  

pip install -r requirements.txt 

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


- first migration
./manage.py migrate

- create a unique URL pattern
inside core (project folder) include the path to the urls of the newapp

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('adminsite/', admin.site.urls),
    path('', include('newapp.urls'))
]

inside app folder create a urls.py file and extend the urls to be acessed by newapp
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
]


- create a view in newapp folder
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello World!")

- Django look for templates in some standard folders.
So lets create a template folder inside newapp
And create an html file inside
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Hello World</title>
</head>
<body>
    Hello World!
</body>






