# Online-shop-backend
# 📖 
It is a web based projects backend which provides service for sign-up, sign-in and admin panel. It supports carting, ordering and making invoice of orders. It performs with python-django, REST-Api and Postgresql. 

# 📋 Setup

It is best to use the python `virtualenv` tool to build locally:
- Clone the repository

```shell script
$ git clone https://github.com/Sajaldeb25/Online-shop-backend-.git
$ cd Online-shop-backend-
```
- Create Virtual environment and Install dependencies

```diff
$ virtualenv env
$ source ./env/bin/activate
$ pip install -r requirements.txt
```

- Make `.env` file to the root directory of the project. `.env` file should contains following variables.
```
SECRET_KEY=
ALLOWED_HOSTS=
DEBUG=
SQLITE_URL=
CORS_ALLOWED_ORIGINS=
```

# 📋 Database connection
```shell script
'ENGINE': 'django.db.backends.postgresql',
'NAME': 'shop',
'USER': 'postgres',
'PASSWORD': '12345',
'HOST': 'localhost',
'PORT': '5432'
```


# 📋 Run
```shell script
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```
Then visit [http://localhost:8000/product/](http://localhost:8000) to view backend of the app.

# 📋 Features of the Project

- Two types of user - admin, user
- Product Management
- Monitor Categories of products
- sign in and sign up 
- cart items
- order items
- pagination of products 




# 📋 Folder Structure 
```
Online-shop-backend-
├── shop
│    ├── migrations                                                     - contains all migration history. 
│                  ├── __init__.py                                      - Initial migration
│                  ├── 0001_initial.py                                  - First migration 
│                  ├── 0002_rename_categories_category_rename_products_product.py        
│                  ├── 0003_cartitem.py        
│                  ├── 0004_remove_cartitem_total_cost.py        
│                  ├── 0005_rename_order_by_customer_cartitem_carted_by_customer_and_more.py       
│                  ├── 0006_delete_order.py        
│                  ├── 0007_order.py       
│                  ├── 0008_cartitem_order_flag.py        
│                  ├── 0009_alter_cartitem_order_flag.py        
│                  ├── 0010_product_product_picture.py    
│                  ├── 0011_alter_product_product_picture.py    
│    
│    ├── admin.py     
│    ├── __init__.py  
│    ├── admin.py
│    ├── apps.py
│    ├── models.py              - It contains Task model 
│    ├── serializer.py          - Serialize model data 
│    ├── tests.py
│    ├── urls.py                - Defines path for urls
│    ├── views.py               - All logics 
├── ecommerce
│    ├── __init__.py
│    ├── settings.py            - Contains setting of the project, including REST-Api, Database connection, and app name. 
│    ├── urls.py
│    ├── wsgi.py
│    ├── asgi.py
├── media
│    ├── product_images         - Contains Product images 
│── manage.py                    
│── requirements.txt             - requirements file for install configuration  
|── README.md

```
