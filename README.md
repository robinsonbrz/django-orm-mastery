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

#####
ORM can be describe as libraies

The four building blocks of Django ORM are:

Models/Fields: 
Models are the core of Django ORM. 
Models are defined in Python classes. 
They represent the tables in your database and define the fields that are stored in those tables.
The fields in a model class are defined using the Field class.



Managers: Managers are objects that provide access to the data in your models. 
They allow you to perform CRUD (create, read, update, delete) operations on your data.
The objects manager is the default manager for all models. 
It provides basic CRUD operations on your data. 
You can also create custom managers to provide more specialized access to your data.


QuerySets: QuerySets are objects that represent a set of records from your database. 
They allow you to filter, sort, and slice your data.
They are created using the Model.objects.all() method.
You can then use filters, sorts, and slices to manipulate your data.

Backend (databases systems)
Relationships: 
Relationships allow you to connect different models together. 
This makes it easy to represent complex relationships between data in your database.
There are three types of relationships in Django ORM: one-to-one, one-to-many, and many-to-many.

##
AutoField: This field automatically increments its value for each new record.
BooleanField: This field stores a Boolean value.
CharField: This field stores a string of text.
CommaSeparatedIntegerField: This field stores a comma-separated list of integers.
DateField: This field stores a date value.
DateTimeField: This field stores a date and time value.
DecimalField: This field stores a decimal value.
EmailField: This field stores an email address.
FileField: This field stores a file.
FloatField: This field stores a floating-point value.
ImageField: This field stores an image.
IntegerField: This field stores an integer value.
GenericIPAddressField: This field stores a generic IP address.
OneToOneField: This field stores a one-to-one relationship to another model.
PositiveIntegerField: This field stores a positive integer value.
SlugField: This field stores a slug.
TimeField: This field stores a time value.
URLField: This field stores a URL.
UUIDField: This field stores a UUID value.

### Model managers

In Django ORM, a model manager is an object that provides access to the data in a model. 
It allows you to perform CRUD (create, read, update, delete) operations on your data.

The objects manager is the default manager for all models. 
It provides basic CRUD operations on your data. 
You can also create custom managers to provide more specialized access to your data.
student.objects.all()
student -> Model
objects -> Model manager
filter  -> QuerysetApi Method

###
Queryset is a collection of objects from the database

Retrieve objects from the database

Here are some of the most commonly used Django queryset methods:

all(): Returns all objects in the queryset.
filter(): Returns objects that match the given filter criteria.
exclude(): Returns objects that do not match the given filter criteria.
order_by(): Returns objects in the specified order.
distinct(): Returns unique objects in the queryset.
reverse(): Returns objects in reverse order.
len(): Returns the number of objects in the queryset.
get(): Returns a single object from the queryset.
save(): Saves the changes made to the queryset.

aggregate(): Calculates aggregate values over the queryset.
annotate(): Adds calculated fields to the queryset.
dates(): Returns a queryset of dates that match the given filter criteria.
datetimes(): Returns a queryset of datetimes that match the given filter criteria.
none(): Returns a queryset that contains no objects.
union(): Returns a queryset that contains all of the objects from the two given querysets.
intersection(): Returns a queryset that contains only the objects that are in both of the given querysets.
difference(): Returns a queryset that contains the objects that are in the first queryset but not in the second queryset.
select_related(): Loads related objects eagerly.
prefetch_related(): Loads related objects lazily.
extra(): Adds extra fields to the queryset.
defer(): Defers loading of certain fields.
only(): Loads only certain fields.
using(): Specifies the database to use for the queryset.
select_for_update(): Locks the objects in the queryset for update.
raw(): Executes a raw SQL query.

###
from testapp.models import Students
Student.objects.all()

The following code returns the query created by the last ORM operation
from django.db import connection
print(connection.queries)

Student.objects.filter(firstname = "Eli")

# Django ORM Backends
Hosts  the DB Tables

SQLite -> Pré Configured
PostgresSql
MariaDB
MySql
Oracle

# admin.py file
receives config about fields and string representation that will be shown in django admin

it is usefull to add __str__ of the model to show the object in a string representation  instead of a non readables set of characteres

def __str__(self):
    return f"Name: {self.name}"


# Model verbose name field
is a human readable name to the field

# Field types
field names simple and lower case
if they are multiple words use underscore to separate
Leads to fewer mistakes
Consistency







