# Estudo sobre ORM Django
### Imerssão prática no estudo do ORM Django
Série de anotações e exemplos práticos de várias fontes, como Udemy ORM Mastery,
Django ORM cookbook, Django Durga, blog Gileno Filho e outras fontes. 

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

## The four building blocks of Django ORM are:

### Models/Fields: 

Models are the core of Django ORM. 

Models are defined in Python classes. 

They represent the tables in your database and define the fields that are stored in those tables.

The fields in a model class are defined using the Field class.

### Managers: Managers are objects that provide access to the data in your models. 

They allow you to perform CRUD (create, read, update, delete) operations on your data.

The objects manager is the default manager for all models. 

It provides basic CRUD operations on your data. 

You can also create custom managers to provide more specialized access to your data.


### QuerySets: QuerySets are objects that represent a set of records from your database. 

They allow you to filter, sort, and slice your data.

They are created using the Model.objects.all() method.

You can then use filters, sorts, and slices to manipulate your data.

### Backend (databases systems)

Relationships: 

Relationships allow you to connect different models together. 

This makes it easy to represent complex relationships between data in your database.

There are three types of relationships in Django ORM: one-to-one, one-to-many, and many-to-many.

### Fields

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

https://www.gilenofilho.com.br/como-funciona-o-orm-do-django/
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


# Sample student 2

```Python
from django.db import models


class Student(models.Model):
    rollno=models.IntegerField()
    name=models.CharField(max_length=30)
    dob=models.DateField()
    marks=models.IntegerField()
    email=models.EmailField()
    phonenumber=models.IntegerField
```

```Python

from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
```

```Python
from django.shortcuts import render
from .forms import StudentForm

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = StudentForm()
    return render(request, 'add_student.html', {'form': form})

```

```Python
{% extends 'base.html' %}

{% block content %}
<div class="container mt-5">
    <h2>Add Student</h2>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit" class="btn btn-primary">Add Student</button>
    </form>
</div>
{% endblock %}


```

<details>
  <summary>54. Section Introduction</summary>
</details>

___


<details>
  <summary>55. Section setup guide - Codebase-1</summary>


```Python

from django.db import models
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=150, unique=True)
    is_active = models.BooleanField( default=False)
    parent = TreeForeignKey(
        "self",
        on_delete=models.PROTECT,
        related_name="children",
        null=True,
        blank=True,
    )

    class MPTTMeta:
        order_insertion_by = ["name"]

    class Meta:
        ordering = ["name"]
        verbose_name_plural = _("categories")

    def __str__(self):
        return self.name


class Product(models.Model):
    web_id = models.CharField(
        max_length=50,
        unique=True,
    )
    slug = models.SlugField(max_length=255)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    category = models.ManyToManyField(Category)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
    )
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Brand(models.Model):
    brand_id = models.PositiveIntegerField(primary_key=True, db_column="brand_id")
    name = models.CharField(
        max_length=255,
        unique=True,
    )
    nickname = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ProductAttribute(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
    )
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class ProductType(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
    )

    product_type_attributes = models.ManyToManyField(
        ProductAttribute,
        related_name="product_type_attributes",
        through="ProductTypeAttribute",
    )

    def __str__(self):
        return self.name


class ProductAttributeValue(models.Model):
    product_attribute = models.ForeignKey(
        ProductAttribute,
        related_name="product_attribute",
        on_delete=models.PROTECT,
    )
    attribute_value = models.CharField(max_length=255)


class ProductInventory(models.Model):
    sku = models.CharField(
        max_length=20,
        unique=True,
    )
    upc = models.CharField(
        max_length=12,
        unique=True,
    )
    product_type = models.ForeignKey(
        ProductType, 
        related_name="product_type", 
        on_delete=models.PROTECT
    )
    product = models.ForeignKey(
        Product, 
        related_name="product", 
        on_delete=models.PROTECT
    )
    brand = models.ForeignKey(
        Brand,
        related_name="brand",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    attribute_values = models.ManyToManyField(
        ProductAttributeValue,
        related_name="product_attribute_values",
        through="ProductAttributeValues",
    )
    is_active = models.BooleanField(default=False)
    is_default = models.BooleanField(default=False)
    retail_price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        error_messages={
            "name": {
                "max_length": _("the price must be between 0 and 999.99."),
            },
        },
    )
    store_price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        error_messages={
            "name": {
                "max_length": _("the price must be between 0 and 999.99."),
            },
        },
    )
    sale_price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        error_messages={
            "name": {
                "max_length": _("the price must be between 0 and 999.99."),
            },
        },
    )
    is_on_sale = models.BooleanField(default=False)
    is_digital = models.BooleanField(default=False)
    weight = models.FloatField()
    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
    )
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.sku


class Media(models.Model):
    product_inventory = models.ForeignKey(
        ProductInventory,
        on_delete=models.PROTECT,
        related_name="media",
    )
    img_url = models.ImageField()
    alt_text = models.CharField(max_length=255)
    is_feature = models.BooleanField(default=False)
    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
    )
    updated_at = models.DateTimeField(auto_now=True)


class Stock(models.Model):
    product_inventory = models.OneToOneField(
        ProductInventory,
        related_name="product_inventory",
        on_delete=models.PROTECT,
    )
    last_checked = models.DateTimeField(
        null=True,
        blank=True,
    )
    units = models.IntegerField(default=0)
    units_sold = models.IntegerField(default=0)


class ProductAttributeValues(models.Model):
    attributevalues = models.ForeignKey(
        "ProductAttributeValue",
        related_name="attributevaluess",
        on_delete=models.PROTECT,
    )
    productinventory = models.ForeignKey(
        ProductInventory,
        related_name="productattributevaluess",
        on_delete=models.PROTECT,
    )

    class Meta:
        unique_together = (("attributevalues", "productinventory"),)


class ProductTypeAttribute(models.Model):
    product_attribute = models.ForeignKey(
        ProductAttribute,
        related_name="productattribute",
        on_delete=models.PROTECT,
    )
    product_type = models.ForeignKey(
        ProductType,
        related_name="producttype",
        on_delete=models.PROTECT,
    )

    class Meta:
        unique_together = (("product_attribute", "product_type"),)
```
</summary>
</details>

___

<details>
  <summary>56. Insert data into a single table with create()</summary>

### Insert into single table with create()

```python
from inventory.models import Brand, Category
from django.db import connection
from django.db import reset_queries

x = Brand.objects.create(brand_id=1,name='nike')

# Deletando todos
Brand.objects.all().delete()

x = Brand.objects.create(brand_id=1,name='nike')


x = Category.objects.create(name='Trainers', slug='trainers', is_active=True)

connection.queries
reset_queries()
```
</details>

___

<details>
  <summary>57. Insert data into a single table with save()</summary>

### Insert into single table with save()

```python
Model.save(
    force_insert=False, 
    force_update=False, 
    using=DEFAULT_DB_ALIAS, 
    update_fields=None
    )

from inventory.models import Brand, Category
Brand.objects.all()
Brand.objects.all().delete()

x = Brand(brand_id=1000)
x.name="nike1000"
x.save()

x = Category(name="trainers1", slug="trainers1", is_active=True)
x.save()

Category.objects.all()

```
</details>

___

<details>
  <summary>58. Explore the difference between save() and create()</summary>

### Explore the difference between save() and create()

```python
from inventory.models import Brand, Category
from django.db import connection, reset_queries

Brand.objects.all().delete()
Brand.objects.create(brand_id=1,name="nike")

Brand(brand_id=1000,name="nike1000").save()

Category.objects.all().delete()

Category.objects.create(id=3, name='Trainers', slug='trainers', is_active=True)

x = Category(id=3, name='Trainers100', slug='trainers1000', is_active=True)
x.save()

connection.queries
reset_queries()

Category.objects.create(name='Trainers1000', slug='trainers1000', is_active=True)

Brand.objects.create(brand_id=1,name="nike")
Brand.objects.create(brand_id=1,name="nike")
Trying to insert the same data into Unique field raises an error using create

However sing save() it doesnt raise an error 
Brand(brand_id=1, name="nike").save()
Brand(brand_id=1, name="nike").save()

# this way we can update the value of the field with id =1
Brand(brand_id=1, name="nike").save()

```
shows the last queries generated by the ORM
connection.queries

```
{
    'sql': 
    'SELECT "inventory_brand"."brand_id", 
        "inventory_brand"."name", 
        "inventory_brand"."nickname" 
    FROM "inventory_brand" LIMIT 21', 
        'time': '0.000'}, 
```

```
{
    'sql': 
    'UPDATE "inventory_brand" 
        SET "name" = \'nike\', "nickname" = \'\' 
        WHERE "inventory_brand"."brand_id" = 1', 
        'time': '0.006'}
```
</details>

___

<details>
  <summary>59. SQL Insert - Executing custom SQL Inserts </summary>
 
 ### SQL Insert - Executing custom SQL Insert

```python
from inventory.models import Brand
from django.db import connection, transaction
from django.db import reset_queries

cursor = connection.cursor()
cursor.execute(
    "INSERT INTO inventory_brand (brand_id, name, nickname) 
    VALUES (%s, %s, %s)", ['10','Reebok','nickname teste']
)

#exibe as queries
connection.queries
# reseta as queries 
reset_queries()

```
</details>

___

<details>
  <summary>60. Insert into single table with foreign key</summary>
 
 ### Insert into single table with foreign key

```python
from inventory.models import Product, ProductInventory, ProductType, Brand
Brand.objects.all().delete()
Brand.objects.create(brand_id=1,name="nike")

Product.objects.all().delete()
Product(
    web_id='1234',
    slug='nike-shoe-1',
    name='nike-shoe-1',
    description='ex2',
    is_active=True
).save()

ProductType.objects.create(name="shoe")

ProductInventory.objects.create(
    sku='123',
    upc='123',
    product_type_id=1,
    product_id=2,
    brand_id=1, 
    retail_price='10.00', 
    store_price='10.00', 
    sale_price='10.00', 
    weight='100'
)

```
</details>

___

<details>
  <summary>61. SQL Insert - Working with datetime fields and foreign keys</summary>


### SQL Insert - working with datetime fields

```python
from inventory.models import Product, ProductInventory, ProductType, Brand
from django.db import connection

# Delete previous data
ProductInventory.objects.all().delete()
Brand.objects.all().delete()
Product.objects.all().delete()
ProductType.objects.all().delete()


Brand.objects.create(brand_id=1,name="nike")
Product(
    web_id='1234',
    slug='nike-shoe-1',
    name='nike-shoe-1',
    description='ex2',
    is_active=True
).save()
ProductType.objects.create(name="shoe")

cursor = connection.cursor()
cursor.execute(
    "INSERT INTO inventory_productinventory(sku,upc,product_type_id,product_id,brand_id,is_active,is_default,retail_price,store_price,sale_price,is_on_sale,is_digital,weight,created_at,updated_at) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",['123','123',1,1,1,True,True,'10.00','10.00','10.00',True,True,'100','2022-06-08 13:38:15.019291','2022-06-08 13:38:15.019291'])

import datetime
datetime_object = datetime.datetime.now()
print(datetime_object)
# >>>  2022-06-08 13:38:15.019291

```

### Objetos datetime
Um objeto datetime é um único objeto contendo todas as informações de um objeto date e um objeto time.

Assim como um objeto date, datetime assume o atual calendário Gregoriano estendido em ambas as direções; assim como um objeto time, datetime assume que existem exatamente 3600*24 segundos em cada dia.


```python
>>> from datetime import date
>>> date.fromisoformat('2019-12-04')
datetime.date(2019, 12, 4)
```
class datetime.date
Uma data ingênua idealizada, presumindo que o atual calendário Gregoriano sempre foi, e sempre estará em vigor. Atributos: year, month, e day.

class datetime.time
Um horário ideal, independente de qualquer dia em particular, presumindo que todos os dias tenham exatamente 24*60*60 segundos. (Não há noção de “segundos bissextos” aqui.) Atributos: hour, minute, second, microsecond e tzinfo.

class datetime.datetime
Uma combinação de uma data e uma hora. Atributos: year, month, day, hour, minute, second, microsecond, e tzinfo.

class datetime.timedelta
Uma duração que expressa a diferença entre duas instâncias date, time ou datetime para resolução de microssegundos.



date2 = date1 + timedelta
date2 é movida para frente no tempo se timedelta.days > 0, ou para trás se timedelta.days < 0. Posteriormente date2 - date1 == timedelta.days. timedelta.seconds e timedelta.microseconds são ignorados. OverflowError é levantado se date2.year for menor que MINYEAR ou maior que MAXYEAR.
timedelta.seconds e timedelta.microseconds são ignoradas.

date2 = date1 - timedelta
timedelta = date1 - date2
date1 < date2

date.weekday()
Retorna o dia da semana como um inteiro, onde Segunda é 0 e Domingo é 6. Por exemplo, date(2002, 12, 4).weekday() == 2, uma Quarta-feira. Veja também isoweekday().

date.isoweekday()
Retorna o dia da semana como um inteiro, onde Segunda é 1 e Domingo é 7. Por exemplo, date(2002, 12, 4).isoweekday() == 3, uma Quarta-feira. Veja também weekday(), isocalendar().

Construtor:

class datetime.datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0)
Os argumentos year, month e day são obrigatórios. tzinfo pode ser None, ou uma instância de subclasse de tzinfo. Os argumentos remanescentes devem ser inteiros nos seguintes intervalos:

MINYEAR <= year <= MAXYEAR,

1 <= month <= 12,

1 <= day <= número de dias no mês e ano fornecidos,

0 <= hour < 24,

0 <= minute < 60,

0 <= second < 60,

0 <= microsecond < 1000000,

fold in [0, 1].

datetime.year
Entre MINYEAR e MAXYEAR incluindo extremos.

datetime.month
Entre 1 e 12 incluindo extremos.

datetime.day
Entre 1 e o número de dias no mês especificado do ano especificado.

datetime.hour
No intervalo range(24).

datetime.minute
No intervalo range(60).

datetime.second
No intervalo range(60).

datetime.microsecond
No intervalo range(1000000).

</details>

___

<details>
  <summary>62. Insert data into a single table with a many-to-many relationship</summary>

Insert into single table with many-to-many relationship table

```python
from inventory.models import Product, Category, ProductInventory, Brand, ProductType

ProductInventory.objects.all().delete()
Brand.objects.all().delete()
Product.objects.all().delete()
ProductType.objects.all().delete()
Category.objects.all().delete()

x = Product(
    web_id='12345',
    slug='ex1',
    name='ex1',
    description='ex1',
    is_active=True
)
x.save()
y = Category(name='Flip-Flops', slug='flipflops', is_active=True)
y.save()

x = Product(
    web_id='123456780',
    slug='ex100000',
    name='ex100000',
    description='ex10000',
    is_active=True
)
x.save()

x = Product.objects.get(id=4)
y = Category.objects.get(id=1)

x.category.add(Category.objects.get(id=1))

y = Category(
    name='Flip-Flops2', 
    slug='flipflops2', 
    is_active=True
)
y.save()

y = Category.objects.all()
# unpack all categories in a Product
x.category.add(*y)

```
</details>

___

<details>
  <summary>63. SQL Insert – Working with many-to-many relationships</summary>
Insert into single table with many-to-many relationship table

```python
from inventory.models import Product, Category, ProductInventory, Brand, ProductType
from django.db import connection, reset_queries

ProductInventory.objects.all().delete()
Brand.objects.all().delete()
Product.objects.all().delete()
ProductType.objects.all().delete()
Category.objects.all().delete()

x = Product(
    web_id='123456780',
    slug='ex100000',
    name='ex100000',
    description='ex10000',
    is_active=True
    )
x.save()
y = Category(name='Flip-Flops', slug='flipflops', is_active=True)
y.save()
x.category.add(y)

cursor = connection.cursor()
cursor.execute("INSERT INTO inventory_product (web_id,slug,name,description,is_active,created_at,updated_at) VALUES (%s,%s,%s,%s,%s,%s,%s)", ['123456','ex4','ex4','ex4',True,'2022-05-31 16:08:08.725532','2022-05-31 16:08:08.725532'])

cursor.execute("INSERT INTO inventory_category (name,slug,is_active,lft,rght,tree_id,level) VALUES (%s, %s, %s, %s, %s, %s, %s)", ['Flip-Flops','flipflops', True, 1,2,1,0])

cursor.execute("INSERT INTO inventory_product_category (product_id,category_id) VALUES (%s, %s)", [8,4])

connection.queries
reset_queries()

```
</details>

___

<details>
  <summary>64. Insert data into multiples tables & using atomic operations</summary>

atomic operationsallows us to change data into the database only if all of the operations run succesfully
    try:
        with transaction.atomic():



In one statement: No
In one transaction: Yes

```python
from inventory.models import Product, ProductInventory, Brand, ProductType, Stock

Product.objects.all().delete()
Brand.objects.all().delete()
ProductType.objects.all().delete()
ProductInventory.objects.all().delete()

Product.objects.create(
    web_id='123',slug='ex1',
    name='ex1',
    description='ex10000',
    is_active=True
    )

Brand.objects.create(brand_id=1,name='ex1')

ProductType.objects.create(name="shoe")

ProductInventory.objects.create(
    sku='123',upc='123',
    product_type_id=1,
    product_id=2,
    brand_id=1,
     retail_price='10.00',
     store_price='10.00',
     sale_price='10.00',
     weight='100'
     )

Stock.objects.create(product_inventory_id=1,units=100)

```


```python

# url.py
from inventory import views
path('test/', views.example)

# view example
def example(request):

from django.http import HttpResponse
from inventory.models import ProductInventory, Stock
from django.db import IntegrityError, transaction


def new(request):

    try:
        with transaction.atomic():
            ProductInventory.objects.create(
                sku='1234',
                upc='1234',
                product_type_id=3,
                product_id=11,
                brand_id=1,
                retail_price='10.00',
                store_price='10.00',
                sale_price='10.00',
                weight='100'
            )

            Stock.objects.create(product_inventory_id=6,units=100)
    except IntegrityError:
        return HttpResponse("Error")

    return HttpResponse("Hi")
```
</details>

___

<details>
  <summary>65. Insert data into a single table with a one-to-one relationship</summary>
Insert into single table with one-to-one relationship

```python
from inventory.models import Product, ProductInventory, Brand, ProductType, Stock

Product.objects.create(
    web_id='123',
    slug='ex1',
    name='ex1',
    description='ex1',
    is_active=True
    )
Brand.objects.create(
    brand_id=1,
    name='ex1'
    )
ProductType.objects.create(name="shoe")
ProductInventory.objects.create(
    sku='123',
    upc='123',
    product_type_id=1,
    product_id=1,
    brand_id=1,
    retail_price='10.00',
    store_price='10.00',
    sale_price='10.00',
    weight='100'
    )

Stock.objects.create(product_inventory_id=1,
units=100)

```
</details>

___

<details>
  <summary>66. Insert multiple objects into single table – bulk create</summary>
Insert multiple objects into single table – bulk create

```python
from inventory.models import Brand
Brand.objects.all().delete()

data = [{'brand_id':3,'name': '3'},{'brand_id':4,'name': '5'}]

# Bulk create receives a list
Brand.objects.bulk_create([Brand(**ab) for ab in data])

```

Second example
```python
Category.objects.bulk_create(
    [Category(name="God"),
     Category(name="Demi God"),
     Category(name="Mortal")]
)
```
</details>

___
<details>
  <summary>67. Query Profiling – bulk_create() vs create() performance analysis</summary>

Query Profiling - bulk_create vs create performance 

```python
from inventory.models import Brand
from django.db import connection, transaction
from django.db import reset_queries
'''

cProfile is a Python module that can be used to profile Python code. 
It provides detailed information about the time spent 
in each function and the number of times each function is called. 
'''
import cProfile

# from inventory import views

def using_multiple_inserts():
    for n in range(10000):
        Brand.objects.create(name=f"{n}")

p = cProfile.Profile()
p.runcall(using_multiple_inserts)
p.print_stats(sort='tottime')

def using_bulk_create():
    Brand.objects.bulk_create([Brand(name=f"{n}") for n in range(10000)])

p = cProfile.Profile()
p.runcall(using_bulk_create)
p.print_stats(sort='tottime')


Brand.objects.all().delete()
connection.queries
reset_queries()

```
</details>

___

<details>
  <summary>68. Creating and automating a set of Django Fixtures</summary>

Query Profiling - bulk_create vs create performance

```python

from django.core.management import call_command
from django.core.management.base import BaseCommand


# dumpdata > db.json # all
# dumpdata admin > admin.json # app
# dumpdata admin.logentry > logentry.json # table

# dumpdata auth.user --indent 2 > user.json # indent

class Command(BaseCommand):
    def handle(self, *args, **kwargs):

        # call_command method calls "python manage.py" followed by the command
        call_command("makemigrations")
        call_command("migrate")
        call_command("loaddata", "db_admin_fixture.json")
        call_command("loaddata", "db_category_fixture.json")
        call_command("loaddata", "db_product_fixture.json")
        call_command("loaddata", "db_category_product_fixture.json")
        call_command("loaddata", "db_type_fixture.json")
        call_command("loaddata", "db_brand_fixture.json")
        call_command("loaddata", "db_product_inventory_fixture.json")
        call_command("loaddata", "db_media_fixture.json")
        call_command("loaddata", "db_stock_fixture.json")
        call_command("loaddata", "db_product_attribute_fixture.json")
        call_command("loaddata", "db_product_attribute_value_fixture.json")
        call_command("loaddata", "db_product_attribute_values_fixture.json")
        call_command("loaddata", "db_product_type_attribute_fixture.json")

```

inventory_brand.json
``` json
[
  {
    "model": "inventory.brand",
    "pk": 1,
    "fields": {
      "name": "nike",
      "nickname": "nike"
    }
  },
  {
    "model": "inventory.brand",
    "pk": 2,
    "fields": {
      "name": "nike2",
      "nickname": "nike2"
    }
  }
]
```
import data from a json to the DB
python manage.py loaddata inventory_brand
</details>

___


<details>
  <summary>69. Section Introduction</summary>
</details>

___

<details>
  <summary>70. Section setup guide (Codebase-2)</summary>
</details>

___

<details>
  <summary>71. Return all objects from a single table – all()</summary>


Return all data from a single table

```python
from ecommerce.inventory.models import Brand, Category
Brand.objects.all()
Brand.objects.all().query

```
</details>

___

<details>
  <summary>72. SQL – Return all objects from a single table</summary>

A queryset is almost a list of objects

SQL – Return all objects from a single table

```python
from inventory.models import Brand, Category
from django.db import connection
from django.db import reset_queries

cursor = connection.cursor()
x = cursor.execute("SELECT name FROM inventory_brand")
for i in x:
    print(i)

x = Brand.objects.raw('SELECT * FROM inventory_brand')
for i in x:
    print(i)


connection.queries
reset_queries()
```
</details>

___

<details>
  <summary>73. Retrieving single objects from a single table – get()</summary>


get does not return a queryset, it returns a object
One object from the DB

If there are more than one object to return it raises an error
If it does not exist it raises an error as well


SQL – Retrieving single objects from a single table

```python
from ecommerce.inventory.models import Brand, Category
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned


Brand.objects.get(id=1)
Brand.objects.all()
Brand.objects.create(name="361")

x = Brand.objects.get(id=1)
Brand.objects.get(id=100)

```

Showing objects fields and values:
pprint(vars(s))
{'age': 14, 'id': 23, 'name': 'Alice'}


calling the __dict__ attribute

print(s.__dict__)
</details>


___

<details>
  <summary>74. SQL – Return single objects from a single table</summary>

SQL – Retrieving single objects from a single table

```python
from inventory.models import Brand
from django.db import connection
from django.db import reset_queries

Brand.objects.bulk_create([Brand(name='Reebok'),Brand(name='Puma')])

Brand.objects.get(name='Nike')

x = Brand.objects.raw('SELECT * FROM inventory_brand WHERE name="Reebok"')
for i in x:
    print(i)

x = Brand.objects.raw('SELECT * FROM inventory_brand WHERE name="Reebok" OR id=2')
for i in x:
    print(i)

connection.queries
reset_queries()

```
</details>

___

<details>
  <summary>75. Filter & Exclude - Retrieving specific objects</summary>

Filter & Exclude - Retrieving specific objects
Can filter fields like i name or any field

Within Filter we use lookup parameters

```python
from ecommerce.inventory.models import Brand

Brand.objects.all()
Brand.objects.get(id=1)

Brand.objects.all().filter(id=1)
Brand.objects.all().filter(id=1,name="361")
# like an and operator and and andand 
Brand.objects.filter(id=1).filter(name="361")

# like SQL or operator or or or or or
Brand.objects.filter(id=1,name="361") | Brand.objects.filter(id=2) | Brand.objects.filter(id=3)

# lookup operators
Brand.objects.all().filter(id__lte=10)
Brand.objects.all().filter(name__startswith="a")

# excluding
Brand.objects.all().exclude(id=1)
Brand.objects.all().exclude(name__startswith="a")

```
</details>

___

<details>
  <summary>76. SQL – Filter retrieving objects – filter()</summary>

SQL – Return single objects from a single table

```python
from ecommerce.inventory.models import Brand
Brand.objects.all()
x = Brand.objects.raw("SELECT * FROM inventory_brand WHERE id=1 AND name='361' OR id=2")
x = Brand.objects.raw("SELECT * FROM inventory_brand WHERE id!=1")

```
</details>

___

<details>
  <summary>77. Retrieve objects from multiple tables through a foreign key relationship</summary>

Filter & Exclude - Retrieving specific objects

```python
from ecommerce.inventory.models import Brand

Brand.objects.all()
Brand.objects.get(id=1)

Brand.objects.all().filter(id=1)
Brand.objects.all().filter(id=1,name="361")
Brand.objects.filter(id=1).filter(name="361")
Brand.objects.filter(id=1,name="361") | Brand.objects.filter(id=2) | Brand.objects.filter(id=3)
Brand.objects.all().filter(id__lte=10)
Brand.objects.all().filter(name__startswith="a")

Brand.objects.all().exclude(id=1)
Brand.objects.all().exclude(name__startswith="a")

```
# Muito importante Reverse lookUp
# Muito importante Reverse lookUp
# Muito importante Reverse lookUp
# Muito importante Reverse lookUp
Must have a related name

Retrieve objects from multiple tables through a foreign key relationship
Retrieve from different tables 

```python
from ecommerce.inventory.models import Product, ProductInventory, Brand, Media, Category
from django.db import connection, reset_queries

x = ProductInventory.objects.filter(brand_id__name="a.x.n.y.")
x = Brand.objects.filter(brand__id=8)

x = Product.objects.filter(category_id=4)

x = Product.objects.filter(category_id__name="sport and fitness")

x = Category.objects.filter(product__name="widstar running sneakers")

x = ProductInventory.objects.filter(product_id__category_id__name="boots")

x = Category.objects.filter(category__product__id=1)

connection.queries
reset_queries()

```
</details>

___

<details>
  <summary>78. SQL - Retrieve objects foreign key relationship</summary>

SQL - Retrieve objects foreign key relationship

```python

from ecommerce.inventory.models import Product, ProductInventory, Brand, Media, Category
from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import PostgresLexer
from sqlparse import format

x = ProductInventory.objects.filter(product_id__slug='widstar-running-sneakers')

x = ProductInventory.objects.raw("SELECT * FROM inventory_productinventory INNER JOIN inventory_product ON inventory_productinventory.product_id = inventory_product.id WHERE inventory_product.slug = 'widstar-running-sneakers'")

formatted = format(str(x.query), reindent=True)
print(highlight(formatted, PostgresLexer(), TerminalFormatter()))

```



</details>

___

![How to use joins graphically explained](imgs/joins-mysql.jpg)

Joins Graphically explained

___



<details>
  <summary>79. Retrieve objects from multiple tables through a one-to-one relationship</summary>

Retrieve objects from multiple tables through a one-to-one relationship

```python
from ecommerce.inventory.models import ProductInventory, Stock

x = Stock.objects.filter(product_inventory_id__store_price=92)

x = ProductInventory.objects.filter(product_inventory__units=135)

```
</details>

___

<details>
  <summary>80. Retrieve objects from multiple tables through a many-to-many relationship</summary>

Retrieve objects from multiple tables through a one-to-one relationship

```python
from ecommerce.inventory.models import ProductInventory, ProductAttributeValue, ProductAttribute, ProductType

x = ProductAttributeValue.objects.filter(product_attribute_values__id=1)

ProductAttribute.objects.filter(product_attribute__product_attribute_values__id=1)

ProductInventory.objects.filter(attribute_values__product_attribute__name="woman-shoe-size").count()

ProductInventory.objects.filter(product_type__product_type_attributes__name="woman-shoe-size").count()

```
</details>

___


<details>
  <summary>81. Section Introduction</summary>

</details>

___

<details>
  <summary>82. Section setup guide (Codebase-2)</summary>

Category has now a foreign key to Product
And the relation is not many to many anymore
</details>

___

<details>
  <summary>83. Modify existing data for a specified record in a table</summary>

Performs an SQL update query for specified fields update()

```python
from ecommerce.inventory.models import Brand

Brand.objects.filter(id=1).update(name="newdata")

Brand.objects.filter(id__range=(1,5)).update(name="newdata")

```
Basically is filter and then .update()
</details>

___

<details>
  <summary>84. Implementing update_or_create()</summary>

Update data or create if it doesnt exist
update_or_create()
Return the object and 
True if created or 
False it it was not created but updated


```python
from ecommerce.inventory.models import Brand

Brand.objects.filter(id=1).update(name="a.n.a")

Brand.objects.update_or_create(id=1, name="veryacademy")

Brand.objects.update_or_create(name="veryacademy", nickname="new")

Brand.objects.update_or_create(name="veryacademy", nickname="new", defaults={"nickname":"newnickname"})

```
</details>

___

<details>
  <summary>85. bulk_update records in a single table</summary>

Bulk Update

```python
from inventory.models import Brand

y = [ Brand.objects.get(id=1) ]
y[0].name = "something"

Brand.objects.bulk_update(y, ["name"])

data = [(1,'aaa'),(2,'bbb')]
id_set = [id for id, name in data]
brand_to_update = Brand.objects.filter(id__in=id_set)

new_update = []
for brand in brand_to_update:
    brand.name = next(name for id, name in data if id == brand.id)
    new_update.append(brand)
    print(brand.name)

Brand.objects.bulk_update(new_update, ['name'])

```
</details>

___

<details>
  <summary>86. Section Introduction</summary>

This setup doesnt have a many to many relationship between Product and category

</details>

___

<details>
  <summary>87. Section setup guide (Codebase-2)</summary>

</details>

___

<details>
  <summary>88. Delete single and multiple objects</summary>

First identify what is going to be deleted
Beware of deleting non intentional data

Delete single object

```python
from inventory.models import Brand
from django.db import connection
from django.db import reset_queries

x = Brand.objects.create(name='Adidas')

Brand.objects.all().delete()

Brand.objects.get(brand_id=1).delete()

Brand.objects.filter(brand_id_2).delete()

# Note sign-posting to FK behavior (possible future referral to Django ORM course focused on building databases/structure)

connection.queries
reset_queries()

```
</details>

___


<details>
  <summary>89. Section introduction</summary>
</details>

___

<details>
  <summary>90. Docker introduction</summary>
</details>

___

<details>
  <summary>91. Installing Docker MacOS</summary>
</details>

___

<details>
  <summary>92. Installing Docker Desktop for Windows 10/11</summary>
</details>

___

<details>
  <summary>93. Create a Postgres Docker container</summary>
</details>

___

<details>
  <summary>94. Configuring Django to work with a PostgreSQL database</summary>
</details>

___


<details>
  <summary>Seção 16:L1: Field lookup Keywords Arguments</summary>
</details>

___

<details>
  <summary>95. Section Introduction</summary>
</details>

___

<details>
  <summary>96. Section setup guide (Codebase-3)</summary>
</details>

___


<details>
  <summary>97. Field lookups</summary>

Uses Postgres Database and Docker Containers

Field Lookups
name__exact
name__iexact
id__exact

```python
from ecommerce.inventory.models import Product
from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import PostgresLexer
from sqlparse import format

def sql(x):
    formatted = format(str(x.query), reindent=True)
    print(highlight(formatted, PostgresLexer(), TerminalFormatter()))


Product.objects.filter()
Product.objects.exclude()
Product.objects.get()

x = Product.objects.filter(id=1)
x = Product.objects.filter(name__exact="widstar running sneakers")
x = Product.objects.filter(name__iexact="Widstar running sneakers")

# Query when no entry or NULL
Product.objects.filter(id__exact=None)

```
</details>

___

<details>
  <summary>98. Field lookup contains</summary>

contains
icontains -> Case insensitive


```python
from ecommerce.inventory.models import Product
from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import PostgresLexer
from sqlparse import format

def sql(x):
    formatted = format(str(x.query), reindent=True)
    print(highlight(formatted, PostgresLexer(), TerminalFormatter()))

x = Product.objects.filter(name__exact="widstar running sneakers")
x = Product.objects.filter(name__iexact="widstar running sneakers")
# %or% Finds any values that have "or" in any position
x = Product.objects.filter(name__contains="widstar running sneakers")
x = Product.objects.filter(name__icontains="widstar running sneakers")
# 'a%o' Finds any values that start with "a" and ends with "o"

```
</details>

___

<details>
  <summary>99. Field lookup with greater or less than</summary>

Greater Than
Lesser Than
Greater Equal Than
Lesser Equal Than
__lt=100
__gt=100
__gte=100
__lte=100


```python
from ecommerce.inventory.models import ProductInventory
from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import PostgresLexer
from sqlparse import format

def sql(x):
    formatted = format(str(x.query), reindent=True)
    print(highlight(formatted, PostgresLexer(), TerminalFormatter()))

x = ProductInventory.objects.filter(retail_price__lt=100)
x = ProductInventory.objects.filter(retail_price__gt=100)
x = ProductInventory.objects.filter(retail_price__gte=100)
x = ProductInventory.objects.filter(retail_price__lte=100)

# greater than 100 and less than 300 
x = ProductInventory.objects.filter(retail_price__gt=100) | ProductInventory.objects.filter(retail_price__lt=300)

```
</details>

___

<details>
  <summary>100. Field lookup with start or end with</summary>

Wildcards 

Contains

```python
from ecommerce.inventory.models import Product
from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import PostgresLexer
from sqlparse import format

def sql(x):
    formatted = format(str(x.query), reindent=True)
    print(highlight(formatted, PostgresLexer(), TerminalFormatter()))

# startswith
# istartswith - case-insensitive starts-with
# endswith
# iendswith

x = Product.objects.filter(name__startswith='a')
x = Product.objects.filter(name__endswith='a')
x = Product.objects.filter(name__startswith='a').filter(name__endswith='a')

# 'a%' start with "a"
# '%a' ends with "a"
# %a% "a" in any position
# _a% "a" in the second position
# a_% "a" and are at least 2 characters in length
# a__% "a" and are at least 3 characters in length
# a%a start with "a" and ends with "a"

```
</details>

___

<details>
  <summary>101. Field lookup range</summary>

Contains

```python
from ecommerce.inventory.models import ProductInventory
from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import PostgresLexer
from sqlparse import format

def sql(x):
    formatted = format(str(x.query), reindent=True)
    print(highlight(formatted, PostgresLexer(), TerminalFormatter()))

x = ProductInventory.objects.filter(retail_price__range=(1,10))
# will return all ProductInventory objects that were:
# created between 2020-01-01 and 2022-10-10, inclusive.
x = ProductInventory.objects.filter(
    created_at__range=('2020-01-01','2022-10-10')
    )

```
</details>

___

<details>
  <summary>102. Field lookup Day Week Month</summary>

Day 
Week 
Month

```python
from ecommerce.inventory.models import ProductInventory
from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import PostgresLexer
from sqlparse import format

def sql(x):
    formatted = format(str(x.query), reindent=True)
    print(highlight(formatted, PostgresLexer(), TerminalFormatter()))

x = ProductInventory.objects.filter(updated_at__day=9)
x = ProductInventory.objects.filter(updated_at__day__lt=9)
x = ProductInventory.objects.filter(updated_at__month__gt=9)
x = ProductInventory.objects.filter(updated_at__month=9)
x = ProductInventory.objects.filter(updated_at__month__gt=9)
x = ProductInventory.objects.filter(updated_at__week__gt=9)
x = ProductInventory.objects.filter(updated_at__week_day__gt=1)

```
</details>

___

<details>
  <summary>Seção 17: L1: QuerySet Ordering and Limiting</summary>
</details>

___

<details>
  <summary>103. Section Introduction</summary>
</details>

___


<details>
  <summary>104. Section setup guide (Codebase-3)</summary>

Ordering a new QuerySet

```python
from ecommerce.inventory.models import Product
from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import PostgresLexer
from sqlparse import format
from django.db import connection, reset_queries

def sql(x):
    formatted = format(str(x.query), reindent=True)
    print(highlight(formatted, PostgresLexer(), TerminalFormatter()))

x = Product.objects.all().values('id')[:10]
x = Product.objects.all().order_by('name').values('name')[:10]
x = Product.objects.all().order_by('-id').values('id')[:10]
x = Product.objects.all().order_by('?').values('id')[:10]

x = Product.objects.all().order_by('id')

x = Product.objects.raw(
    "SELECT * FROM inventory_product ORDER BY inventory_product.id ASC"
)

x = Product.objects.raw(
    "SELECT * FROM inventory_product ORDER BY inventory_product.id DESC"
)

reset_queries()
connection.queries

```
</details>

___


<details>
  <summary>105. Ordering a new QuerySet</summary>

Ordering a new QuerySet

```python
from ecommerce.inventory.models import Product
from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import PostgresLexer
from sqlparse import format
from django.db import connection, reset_queries

def sql(x):
    formatted = format(str(x.query), reindent=True)
    print(highlight(formatted, PostgresLexer(), TerminalFormatter()))

x = Product.objects.all().values('id')[:10]
x = Product.objects.all().order_by('name').values('name')[:10]
x = Product.objects.all().order_by('-id').values('id')[:10]

# ? it is a random ordered
x = Product.objects.all().order_by('?').values('id')[:10]

x = Product.objects.all().order_by('id')

x = Product.objects.raw(
    "SELECT * FROM inventory_product ORDER BY inventory_product.id ASC"
)

x = Product.objects.raw(
    "SELECT * FROM inventory_product ORDER BY inventory_product.id DESC"
)

reset_queries()
connection.queries
```
</details>

___

<details>
  <summary>106. Reverse the output of a new QuerySet</summary>

Reverse a new QuerySet

```python
from ecommerce.inventory.models import Product, Brand
from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import PostgresLexer
from sqlparse import format
from django.db import connection, reset_queries

def sql(x):
    formatted = format(str(x.query), reindent=True)
    print(highlight(formatted, PostgresLexer(), TerminalFormatter()))

x = Brand.objects.all().order_by('id').reverse().values('id')[:10]
x = Product.objects.all().reverse()

x = Product.objects.raw("SELECT * FROM inventory_product ORDER BY inventory_product.id DESC")

reset_queries()
connection.queries

```
</details>

___

<details>
  <summary>107. Return the first or last object matched by the queryset</summary>

Return the first object matched by the queryset

```python
from ecommerce.inventory.models import Product, Brand
from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import PostgresLexer
from sqlparse import format
from django.db import connection, reset_queries

def sql(x):
    formatted = format(str(x.query), reindent=True)
    print(highlight(formatted, PostgresLexer(), TerminalFormatter()))

x = Brand.objects.all().first()
x = Brand.objects.all().last()

x = Brand.objects.all()[:1]

x = Brand.objects.raw(
    "SELECT * FROM inventory_product ORDER BY inventory_product.id ASC LIMIT 1"
    )

reset_queries()
connection.queries

```
</details>

___

<details>
  <summary>108. Return the earliest or latest object matched by the QuerySet</summary>

Return the earliest or latest object matched by the queryset

```python
from ecommerce.inventory.models import Product
from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import PostgresLexer
from sqlparse import format
from django.db import connection, reset_queries

def sql(x):
    formatted = format(str(x.query), reindent=True)
    print(highlight(formatted, PostgresLexer(), TerminalFormatter()))

x = Product.objects.all().values('id').latest('created_at')
x = Product.objects.all().values('id').earliest('created_at')

x = Product.objects.all().latest('created_at')
x = Product.objects.raw("SELECT * FROM inventory_product ORDER BY inventory_product.created_at DESC LIMIT 1")

x = Product.objects.all().earliest('created_at')
x = Product.objects.raw("SELECT * FROM inventory_product ORDER BY inventory_product.created_at ASC LIMIT 1")

reset_queries()
connection.queries

```
</details>

___

<details>
  <summary>109. Limit the objects returned from a QuerySet</summary>

Limiting QuerySets

```python
from ecommerce.inventory.models import Product
from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import PostgresLexer
from sqlparse import format
from django.db import connection, reset_queries

def sql(x):
    formatted = format(str(x.query), reindent=True)
    print(highlight(formatted, PostgresLexer(), TerminalFormatter()))

Product.objects.all().values('id')[:1]
Product.objects.all().values('id')[0:1]
Product.objects.all().values('id')[0:2]
Product.objects.all().values('id')[0]
Product.objects.all().values('id')[1]
Product.objects.all().values('id')[5:10]
Product.objects.all().values('id')[6:10]
Product.objects.all().values('id')[:10:2]
Product.objects.all().values('id')[1:10:2]

x = Product.objects.all()[5:10]

x = Product.objects.raw("SELECT * FROM inventory_product ORDER BY inventory_product.id ASC LIMIT 5 OFFSET 5")

x = Product.objects.all()[1:10:2] #step parameter of Python slice syntax

x = Product.objects.raw("SELECT * FROM inventory_product ORDER BY inventory_product.id ASC LIMIT 9 OFFSET 1")

reset_queries()
connection.queries

```
</details>


___

<details>
  <summary>Seção 18: L1: Practical Exercises & Answers</summary>
</details>

___

<details>
  <summary>110. Section Introduction</summary>
</details>

___

<details>
  <summary>111. Section setup guide (Codebase-4)</summary>
  make build

  And then populate the database
```python
  python manage.py demo-fixtures
```
</details>

___

![Diagrama ER](imgs/DERInventory.png)
Diagrama ER

___

<details>
  <summary>112. Reintroducing the database design and dataset</summary>




</details>

___

```python
class ProductInventory(models.Model):
    sku = models.CharField(
        max_length=20,
        unique=True,
    )
    upc = models.CharField(
        max_length=12,
        unique=True,
    )
    product_type = models.ForeignKey(ProductType, related_name="product_type", on_delete=models.PROTECT)
    product = models.ForeignKey(Product, related_name="product", on_delete=models.PROTECT)



class Product(models.Model):
    web_id = models.CharField(
        max_length=50,
        unique=True,
    )
    slug = models.SlugField(
        max_length=255,
    )
    name = models.CharField(
        max_length=255,
    )
    description = models.TextField(blank=True)
    category = models.ForeignKey(
        Category,
        related_name="product",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    is_active = models.BooleanField(
        default=False,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f"{self.web_id}>{self.name}"


```

<details>
  <summary>113. Retrieve all sub-products for an individual product</summary>

Retrieve a product sub-products

Returning all the products in the ProductInventory for a specific product


```python
from ecommerce.inventory.models import Product
from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import PostgresLexer
from sqlparse import format

def sql(x):
    formatted = format(str(x.query), reindent=True)
    print(highlight(formatted, PostgresLexer(), TerminalFormatter()))


ProductInventory.objects.filter(product_id=1)    

x = ProductInventory.objects.raw(
    "SELECT  inventory_productinventory.id,
            inventory_productinventory.sku,
            inventory_productinventory.upc,
            inventory_productinventory.product_type_id,
            inventory_productinventory.product_id,
            inventory_productinventory.brand_id,
            inventory_productinventory.is_active,
            inventory_productinventory.is_default,
            inventory_productinventory.retail_price,
            inventory_productinventory.store_price,
            inventory_productinventory.is_digital,
            inventory_productinventory.weight,
            inventory_productinventory.created_at,
            inventory_productinventory.updated_at
    FROM inventory_productinventory
    WHERE inventory_productinventory.product_id = 1")

print(sql(x))

```





</details>

___

<details>
  <summary>114. Retrieve a product featured image - 3 tables Relation</summary>
    Tables:
        Media
        ProductInventory  -> product_inventory
        Product -> product_id

```python

x = Media.objects.filter(product_inventory__product_id=1)
len(x)  # returns how many objects are stored

# Returns only the fields that have is_feature = 1
x = Media.objects.filter(is_feature=True).filter(product_inventory__product_id__name="test")
x = Media.objects.filter(is_feature=True,product_inventory__product_id=1)
len(x)


```

```sql
SELECT inventory_media.id,
       inventory_media.product_inventory_id,
       inventory_media.img_url,
       inventory_media.alt_text,
       inventory_media.is_feature,
       inventory_media.created_at,
       inventory_media.updated_at
FROM inventory_media
INNER JOIN inventory_productinventory ON (inventory_media.product_inventory_id = inventory_productinventory.id)
WHERE (inventory_media.is_feature
       AND inventory_productinventory.product_id = 1)

x = Media.objects.raw("SELECT * from inventory_media INNER JOIN inventory_productinventory ON inventory_media.product_inventory_id = inventory_productinventory.id")

x = Media.objects.raw("SELECT * from inventory_media INNER JOIN inventory_productinventory ON inventory_media.product_inventory_id = inventory_productinventory.id WHERE inventory_media.is_feature=True AND inventory_productinventory.product_id=1")

```

</details>

___

<details>
  <summary>115. Retrieve all values associated to a sub-product</summary>
    Reverse many to many
Retrieve all values associated to a sub-product
    
```python

from ecommerce.inventory.models import ProductAttributeValue
from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import PostgresLexer
from sqlparse import format

def sql(x):
    formatted = format(str(x.query), reindent=True)
    print(highlight(formatted, PostgresLexer(), TerminalFormatter()))

x = ProductAttributeValue.objects.filter(product_attribute_values__id=1)

x = ProductAttributeValue.objects.raw("SELECT * FROM inventory_productattributevalue INNER JOIN inventory_productattributevalues ON inventory_productattributevalue.id = inventory_productattributevalues.attributevalues_id WHERE inventory_productattributevalues.productinventory_id=1")
    y = ProductAttributeValue.objects.filter(product_attribute_values__id=1)
```

</details>

___

<details>
  <summary>116. Retrieve the product attributes for a given product type</summary>


Retrieve the product attributes for a given product type

```python
from ecommerce.inventory.models import ProductAttribute
from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import PostgresLexer
from sqlparse import format

def sql(x):
    formatted = format(str(x.query), reindent=True)
    print(highlight(formatted, PostgresLexer(), TerminalFormatter()))

x = ProductAttribute.objects.filter(product_type_attributes=1)

x = ProductAttribute.objects.raw("SELECT * FROM inventory_productattribute INNER JOIN inventory_producttypeattribute ON inventory_productattribute.id = inventory_producttypeattribute.product_attribute_id WHERE inventory_producttypeattribute.product_type_id = 1")

```

</details>

___

<details>
  <summary>117. Retrieve all products associated to product attribute id:1</summary>
  
  Retrieve all products associated to product attribute id:1

```python
from ecommerce.inventory.models import Product
from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import PostgresLexer
from sqlparse import format

def sql(x):
    formatted = format(str(x.query), reindent=True)
    print(highlight(formatted, PostgresLexer(), TerminalFormatter()))

from ecommerce.inventory.models import Product
from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import PostgresLexer
from sqlparse import format

def sql(x):
    formatted = format(str(x.query), reindent=True)
    print(highlight(formatted, PostgresLexer(), TerminalFormatter()))

x = Product.objects.filter(product__attribute_values__product_attribute__id=1).distinct().count()

x = Product.objects.raw("SELECT * FROM inventory_product INNER JOIN inventory_productinventory ON(inventory_product.id = inventory_productinventory.product_id) INNER JOIN inventory_productattributevalues ON (inventory_productinventory.id = inventory_productattributevalues.productinventory_id) INNER JOIN inventory_productattributevalue ON (inventory_productattributevalues.attributevalues_id = inventory_productattributevalue.id) WHERE inventory_productattributevalue.product_attribute_id = 1")

```
</details>

___

<details>
  <summary>118. Retrieve all sub-products that has less than 50 units left in stock</summary>
  Retrieve all sub-products that has less than 50 units left in stock

```python
from ecommerce.inventory.models import ProductInventory
from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import PostgresLexer
from sqlparse import format

def sql(x):
    formatted = format(str(x.query), reindent=True)
    print(highlight(formatted, PostgresLexer(), TerminalFormatter()))

x = ProductInventory.objects.filter(product_inventory__units__lte=50)

x = ProductInventory.objects.raw("SELECT * FROM inventory_productinventory INNER JOIN inventory_stock ON (inventory_productinventory.id = inventory_stock.product_inventory_id) WHERE inventory_stock.units <= 50")

</details>

___

<details>
  <summary>119. Retrieve all sub-products which have been stock checked in the last month</summary>
  Retrieve all sub-products which have been stock checked in the last month

```python
from ecommerce.inventory.models import ProductInventory
from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import PostgresLexer
from sqlparse import format

def sql(x):
    formatted = format(str(x.query), reindent=True)
    print(highlight(formatted, PostgresLexer(), TerminalFormatter()))

x = ProductInventory.objects.filter(product_inventory__last_checked__range=('2020-09-01','2022-10-10'))

x = ProductInventory.objects.raw("SELECT * FROM inventory_productinventory INNER JOIN inventory_stock ON (inventory_productinventory.id = inventory_stock.product_inventory_id) WHERE inventory_stock.last_checked BETWEEN '2020-01-01 00:00:00' AND '2022-10-10 00:00:00'")

```
</details>

___

<details>
  <summary>120. Retrieve all woman shoe products</summary>
Retrieve all sub-products which have been stock checked in the last month

```python
from ecommerce.inventory.models import Product
from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import PostgresLexer
from sqlparse import format

def sql(x):
    formatted = format(str(x.query), reindent=True)
    print(highlight(formatted, PostgresLexer(), TerminalFormatter()))

x = Product.objects.filter(product__product_type__product_type_attributes__id=1).distinct().count()

x = Product.objects.raw("SELECT DISTINCT inventory_product.id FROM inventory_product INNER JOIN inventory_productinventory ON (inventory_product.id = inventory_productinventory.product_id) INNER JOIN inventory_producttype ON (inventory_productinventory.product_type_id = inventory_producttype.id) INNER JOIN inventory_producttypeattribute ON (inventory_producttype.id = inventory_producttypeattribute.product_type_id) WHERE inventory_producttypeattribute.product_attribute_id = 1")

```
</details>

___

<details>
  <summary>121. Retrieve all woman shoes by the xyz brand</summary>
  Retrieve all sub-products which have been stock checked in the last month

```python
from ecommerce.inventory.models import Product
from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import PostgresLexer
from sqlparse import format

def sql(x):
    formatted = format(str(x.query), reindent=True)
    print(highlight(formatted, PostgresLexer(), TerminalFormatter()))

x = Product.objects.filter(product__attribute_values__product_attribute_id=1).count()
x = Product.objects.filter(product__attribute_values__product_attribute_id=1).filter(product__brand_id=1)
x = Product.objects.filter(product__attribute_values__product_attribute_id=1, product__brand_id=1).distinct()

```
</details>

___

<details>
  <summary>122. Retrieve all products associated to the xyz brand</summary>

Retrieve all sub-products which have been stock checked in the last month

```python
from ecommerce.inventory.models import Product
from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import PostgresLexer
from sqlparse import format

def sql(x):
    formatted = format(str(x.query), reindent=True)
    print(highlight(formatted, PostgresLexer(), TerminalFormatter()))

x = Product.objects.filter(product__brand_id=2)

x = Product.objects.raw("SELECT * FROM inventory_product INNER JOIN inventory_productinventory ON (inventory_product.id = inventory_productinventory.product_id) WHERE inventory_productinventory.brand_id = 1")

```

</details>


### Criando um comando personalizado Django
Para executá-lo:

```bash
python manage.py demo-fixtures

```


demo-fixtures.py
```python
from django.core.management import call_command
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'My custom command'
    def handle(self, *args, **options):
        call_command('makemigrations')
        call_command("loaddata", "db_admin_fixture_50.json")

````

O comando call_command executa python manage.py loaddata db_admin_fixture_50.json
json que está na pasta fixtures






