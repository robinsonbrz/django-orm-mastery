https://www.gilenofilho.com.br/como-funciona-o-orm-do-django/
# django-orm-mastery
``` bash
python -m venv .venv   
source .venv/bin/activate  
```
pypi 

``` bash
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
``` bash
source .venv/bin/activate  
pip install -r requirements.txt 
```

Create a new Django project

``` bash
django-admin startproject core .
```
In this experiemnt core is the name of the project
with . creates the core folder in the root folder
without it creates a folder named core and another core folder inside it

``` bash
pip install python-decouple 
```

``` Python
settings.py
from decouple import config

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG')
```
- Create a new app inside core folder
mkdir ./core/newapp                      
./manage.py startapp newapp ./core/newapp

- After create an app it is necessary to register the application in settings.py
``` Python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'newapp',
]
```

- first migration
./manage.py migrate

- create a unique URL pattern
inside core (project folder) include the path to the urls of the newapp
``` Python
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
```

- create a view in newapp folder
``` Python
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello World!")
```

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

##The four building blocks of Django ORM are:

###Models/Fields: 
Models are the core of Django ORM. 
Models are defined in Python classes. 
They represent the tables in your database and define the fields that are stored in those tables.
The fields in a model class are defined using the Field class.

###Managers: Managers are objects that provide access to the data in your models. 
They allow you to perform CRUD (create, read, update, delete) operations on your data.
The objects manager is the default manager for all models. 
It provides basic CRUD operations on your data. 
You can also create custom managers to provide more specialized access to your data.


###QuerySets: QuerySets are objects that represent a set of records from your database. 
They allow you to filter, sort, and slice your data.
They are created using the Model.objects.all() method.
You can then use filters, sorts, and slices to manipulate your data.

###Backend (databases systems)
Relationships: 
Relationships allow you to connect different models together. 
This makes it easy to represent complex relationships between data in your database.
There are three types of relationships in Django ORM: one-to-one, one-to-many, and many-to-many.

###Fields
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
**Queryset** is a collection of objects from the database

Retrieve objects from the database

Here are some of the most commonly used Django **queryset methods:**

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

### Django ORM Backends
Hosts  the DB Tables

SQLite -> Pré Configured
PostgresSql
MariaDB
MySql
Oracle

### admin.py file
receives config about fields and string representation that will be shown in django admin

it is usefull to add __str__ of the model to show the object in a string representation  instead of a non readables set of characteres

def __str__(self):
    return f"Name: {self.name}"


### Model verbose name field
is a human readable name to the field

### Field types
field names simple and lower case
if they are multiple words use underscore to separate
Leads to fewer mistakes
Consistency

### Field options
Can be specific
But there are some important field options like:
    null=True # allows to store empty values     by default it is false
    blank=True # allows to store "" string       by default it is false
    default="default value"
    help_text="auxiliary text" in admin you can view bellow the field, can be used in personalized forms




https://docs.djangoproject.com/en/4.2/ref/models/querysets/
### lookup fields

In Django, a lookup field is a way to filter a QuerySet based on the value of a particular field. For example, you could use the exact lookup field to filter a QuerySet of books to only include books with the title "The Lord of the Rings".

The syntax for a lookup field is as follows:

field_name__lookup_type=value
For example, the following code will filter a QuerySet of books to only include books with the title "The Lord of the Rings":

Python
qs = Book.objects.filter(title__exact="The Lord of the Rings")
Use code with caution. Learn more
Here is a list of the most common lookup fields in Django:

**exact**: The value must match exactly.
**iexact**: The value must match exactly, ignoring case.
**contains**: The value must be contained in the field.
**icontains**: The value must be contained in the field, ignoring case.
**startswith**: The value must start with the field.
**istartswith**: The value must start with the field, ignoring case.
**endswith**: The value must end with the field.
**iendswith**: The value must end with the field, ignoring case.
**in**: The value must be one of the values in the list.
**gt**: The value must be greater than the given value.
**gte**: The value must be greater than or equal to the given value.
**lt**: The value must be less than the given value.
**lte**: The value must be less than or equal to the given value.
You can also use custom lookup fields by creating a subclass of the Lookup class.


Exemplo.objects.filter(situacao="Conservada").values_list('observacao', flat=True)
<QuerySet ['observacao base']>
Exemplo.objects.filter(situacao="Conservada").values_list('observacao')
<QuerySet [('observacao base',)]>

### primary key Relationship
``` Python
brand_id = models.BigAutoField(primary_key=True)
```
Foreign Keys
    **Many to One Relation**
    Example Product and category
    On the table Product we have a category(fk)
    One product One Category
    One Category many products

``` Python
class Category(models.Model):
    name = models.CharField(max_length=50)

class Product(models.Model):
    the_name = models.CharField("Product Name", max_length=100, default="no-name", 
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
```

**on_delete** defines the behavior when deleting a category
When defining models.CASCADE when you delete a category **it will delete all** Products related to this category (This is dangerous and can delete undesirable data)

on_delete=models.PROTECTED prevent delete category until all the products related to this category have been deleted
``` Python
titles = Book.objects.all().values_list('title', flat=True)
```
['Title 1', 'Title 2', 'Title 3', ...]

``` Python
titles = Book.objects.all().values_list('title')
```
[('Title 1',), ('Title 2',), ('Title 3',), ...]

https://books.agiliq.com/projects/django-orm-cookbook/en/latest/one_to_many.html

In relational databases, a one-to-many relationship occurs when a parent record in one table can potentially reference several child records in another table. In a one-to-many relationship, the parent is not required to have child records; therefore, the one-to-many relationship allows zero child records, a single child record or multiple child records. To define a many-to-one relationship, use ForeignKey.:


``` Python
class Article(models.Model):
    headline = models.CharField(max_length=100)
    pub_date = models.DateField()
    reporter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reporter')

    def __str__(self):
        return self.headline

    class Meta:
        ordering = ('headline',)

>>> u1 = User(username='johny1', first_name='Johny', last_name='Smith', email='johny@example.com')
>>> u1.save()
>>> u2 = User(username='alien', first_name='Alien', last_name='Mars', email='alien@example.com')
>>> u2.save()
>>> from datetime import date
>>> a1 = Article(headline="This is a test", pub_date=date(2018, 3, 6), reporter=u1)
>>> a1.save()
>>> a1.reporter.id
13
>>> a1.reporter
<User: johny1>

```
If you try to assign an object before saving it you will encounter a ValueError



### One to One Relationship
In this case one Stock is related to one Product
And the product is related to one Stock
No more than one to one
``` Python
class Product(models.Model):
    name = models.CharField("Product Name", max_length=100, default="no-name", 

class Stock(models.Model):
    units = models.BigIntegerField()
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
```
https://books.agiliq.com/projects/django-orm-cookbook/en/latest/one_to_one.html

One-to-one relationships occur when there is exactly one record in the first table that corresponds to one record in the related table. Here we have an example where we know that each individual can have only one Biological parents i.e., Mother and Father. We already have auth user model with us, we will add a new model UserParent as described below.

``` Python

from django.contrib.auth.models import User

class UserParent(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)

>>> u1 = User.objects.get(first_name='Ritesh', last_name='Deshmukh')
>>> u2 = User.objects.get(first_name='Sohan', last_name='Upadhyay')
>>> p1 = UserParent(user=u1, father_name='Vilasrao Deshmukh', mother_name='Vaishali Deshmukh')
>>> p1.save()
>>> p1.user.first_name
'Ritesh'
>>> p2 = UserParent(user=u2, father_name='Mr R S Upadhyay', mother_name='Mrs S K Upadhyay')
>>> p2.save()
>>> p2.user.last_name
'Upadhyay'
``` 


### Many to Many Relationship
Python ORM creates a intermediary (link) table to connect multiple tables
The intermediary table has 2 foreign keys
This is automatically created by Django

Multiple categories can connect to multiple productcs

``` Python
class Category(models.Model):
    name = models.CharField(max_length=50)

class Product(models.Model):
    name = models.CharField("Product Name", max_length=100, default="no-name")
    category = models.ManyToManyField(Category)
```

https://books.agiliq.com/projects/django-orm-cookbook/en/latest/many_to_many.html

A many-to-many relationship refers to a relationship between tables in a database when a parent row in one table contains several child rows in the second table, and vice versa.

# Model Meta Options

Django Model Meta Options are a set of attributes that can be used to customize the behavior of a Django model. These options can be used to control the name of the database table, the ordering of the fields, and the permissions that are granted to users.

Here are some of the most common Django Model Meta Options:

**db_table:** This option specifies the name of the database table that will be used to store the model data. By default, the database table name is generated from the model class name.
**ordering:** This option specifies the default ordering of the model records in the database. The ordering can be specified as a list of field names, or as a single field name with a sort order (ascending or descending).
**permissions:** This option specifies the permissions that are granted to users for the model. The permissions can be specified as a list of permission names, or as a dictionary of permission names and permission levels.

For a complete list of Django Model Meta Options, please see the Django documentation: https://docs.djangoproject.com/en/stable/ref/models/options/.

**ordering** define the behavior in relation to order the 
``` Python
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_date = models.DateField()

    class Meta:
        db_table = 'books'
        ordering = ['-published_date']
        permissions = [('can_edit', 'Can edit books'), ('can_delete', 'Can delete books')]
```

 database table name should be books, 
 the default ordering of the records should be by the published_date field in descending order, 
 and that the users should have the following permissions: can_edit and can_delete.

# Migrations

Propagating the model changes to the database schema.

# Queries and explain

qs.query                # show the last query


from django.db import connection, reset_queries

connection.queries      # Shows the last queries

reset_queries()         # reset the list of last queries

```Python
>>> print(Blog.objects.filter(title="My Blog").explain(verbose=True, analyze=True))
Seq Scan on public.blog  (cost=0.00..35.50 rows=10 width=12) (actual time=0.004..0.004 rows=10 loops=1)
  Output: id, title
  Filter: (blog.title = 'My Blog'::bpchar)
Planning time: 0.064 ms
Execution time: 0.058 ms
```
## Pretty print SQL 

```bash
pip install Pygments
pip install sqlparse
```

```Python
from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import PostgresLexer
from sqlparse import format
from inventory.models import Brand
```
x = Brand.objects.create(brand_id=1, name='Nike')
sqlformatted = format(str(x.query), reindent=True)
print(highlight(sqlformatted, PostgresLexer(), TerminalFormatter()))



**import:** This module is used to import other modules into the current namespace.
**highlight:** This module provides functions for highlighting code in different formats, such as HTML, LaTeX, and ANSI escape sequences.
**formatters:** This module provides different formatters for the highlight module, such as the TerminalFormatter which is used to highlight code in the terminal.
**lexers:** This module provides lexers for different programming languages, such as the PostgresLexer which is used to tokenize Postgres SQL queries.



```Python
from ecommerce.inventory.models import Brand
from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import PostgresLexer
from sqlparse import format

def sql(x):
    formatted =format(str(x.query), reindent=True)
    print(highlight(formatted, PostgresLexer(), TerminalFormatter()))

# count retuns quantity of objects
x = Brand.objects.all().count()

x = Brand.objects.filter(id=1).values('name')

```


## 7. How to convert string to datetime and store in database?

We can convert a date-string and store it in the database using django in many ways. Few of them are discussed below. Lets say we have a date-string as “2018-03-11” we can not directly store it to our date field, so we can use some dateparser or python library for it.
```Python
>>> user = User.objects.get(id=1)
>>> date_str = "2018-03-11"
>>> from django.utils.dateparse import parse_date // Way 1
>>> temp_date = parse_date(date_str)
>>> a1 = Article(headline="String converted to date", pub_date=temp_date, reporter=user)
>>> a1.save()
>>> a1.pub_date
datetime.date(2018, 3, 11)
>>> from datetime import datetime // Way 2
>>> temp_date = datetime.strptime(date_str, "%Y-%m-%d").date()
>>> a2 = Article(headline="String converted to date way 2", pub_date=temp_date, reporter=user)
>>> a2.save()
>>> a2.pub_date
```
datetime.date(2018, 3, 11)


___

# Student case 

```Python
 from django.db import models



 class Student(models.Model):
    name=models.CharField(max_length=30)
    marks=models.IntegerField()
```

```Python
# views.py
from django.shortcuts import render
from testapp.models import Student


def studentview(request):
 student_list=Student.objects.order_by('marks')
 my_dict={'student_list':student_list}
    return render(request,'testapp/students.html',context=my_dict)
```
