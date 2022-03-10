# API WITH DJANGO REST FRAMEWORK AND MYSQL
Django REST framework is a powerful and flexible toolkit for building Web APIs. MySQL is a relational database management system (RDBMS) developed by Oracle that is based on structured query language (SQL).

## Requirements
- Python 3.8.6
- Django 3.2.4
- Django REST Framework
- mysqlclient 2.1.0
- mysql

## Installation
After you cloned the repository, you need to create a virtual environment. You can do this by running the command.
```sh
python -m venv env
```

## Database

```sh
from django.db import models
class Category(models.Model):
    name = models.CharField(max_length=100)
class Product(models.Model):
    name = models.CharField(max_length=50)
    url_image = models.CharField(max_length=200)
    price = models.FloatField()
    discount = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
```

## Api Rest
### Get all products
```sh
http://localhost:8000/api/products/
```

## Demo
the Api REST was deployed to [Heroku](https://dashboard.heroku.com/).

[Live Demo - Api REST](https://api-rest-bsale.herokuapp.com/api/products/)


## Running the Application
Create the DB tables first:
```sh
python manage.py migrate
```
## Run the development web server:
```sh
python manage.py runserver 8080
```


