# Chapter 

## The default database in Django

[SQLite](https://builtin.com/data-science/sqlite) is the default database used by Django. SQLite is a lightweight embedded databases that does not require installation of a Relational Database Management Service (RDMS) like Postgresql. Being a lightweight system, it has less sophisticated administrative configurations. 

Sqlite is already set by default in your `settings.py` file like so:

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


```

## Installing postgresql

First of all, before connecting Postgresql to Django, you will have to install the Postgresql application in your local PC from the official [Postgresql website](https://www.postgresql.org/download/). 

Select the right package installer from your system. When installing, ensure you store your database name and password in a safe place as these credentials are always asked from time to time. 

Once the installation process finishes successfully, you have Postgresql installed in your system.


## Connecting postgresql in Django 

Sometimes you may have an app that will be in use quite a lot and frequently. This is where the need for a sturdy database comes in, and Postgresql fits the bill as the best open source database out there. 

To use Postgresql in Django, you will first have to install `psycopg2`. `psycopg2` is the most popular PostgresSQL adapter in Python.

```
pip install psycopg2-binary

```

Now go to `settings.py` file and replace the below default SQLite settings:

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

```

Replace them with this:

```
'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '',
    }
```













