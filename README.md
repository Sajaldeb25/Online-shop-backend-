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

