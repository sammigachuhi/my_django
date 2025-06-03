# Chapter 16

## What is geodjango?

[Geodjango](https://www.lifeingis.com/geodjango-tutorial-series/?mode=grid) is a python module for developing Geographic Information Systems (GIS) applications. A [Geographic Information System (GIS)](https://www.usgs.gov/faqs/what-a-geographic-information-system-gis) is a computer system that analyzes and displays geographically referenced information. It uses data that is attached to a unique location.

Geodjango enables one create geographic web applications using Django. 

To work with Geodjango, you will first have to install Postgresql and PostGIS.

[Postgresql](https://www.enterprisedb.com/postgres-tutorials/why-django-so-impressive-developing-postgresql-and-python?lang=en) is the world's most powerful object-oriented database. The number one reason for us to use Postgresql is because Geodjango will only work with Postgresql, and not spatial lite. Other than that, Postgresql is the preferred database when working with large projects where the number of your app users is far much bigger than just a few tens. 


[PostGIS](https://postgis.net/) extends the capabilities of the PostgreSQL relational database by adding support for storing, indexing, and querying geospatial data. PostGIS features include:

* `Spatial Data Storage`: Store different types of spatial data such as points, lines, polygons, and multi-geometries, in both 2D and 3D data.

* `Spatial Indexing`: Quickly search and retrieve spatial data based on its location.

* `Spatial Functions`: A wide range of spatial functions that allow you to filter and analyze spatial data, measuring distances and areas, intersecting geometries, buffering, and more.

* `Geometry Processing`: Tools for processing and manipulating geometry data, such as simplification, conversion, and generalization.

* `Raster Data Support`: Storage and processing of raster data, such as elevation data and weather data.

* `Geocoding and Reverse Geocoding`: Functions for geocoding and reverse geocoding.

* `Integration`: Access and work with PostGIS using third party tools such as QGIS, GeoServer, MapServer, ArcGIS, Tableau.

## Installing Postgresql 

We will follow the steps from the [Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-22-04) website. 

First let's update our package manager cache by using `apt`:

```
sudo apt update
```

The above code makes sure that the system has sufficient information of about the dependencies of each package. The code does not install any software, it only provides the information of the latest dependencies for each package.

When you run the above code it will provide your system pseudo name and ask for your passord. 

Thereafter, run the following code to install the necessary packages to enable Postgresql run smoothly.

```
sudo apt install python3-pip python3-dev libpq-dev postgresql postgresql-contrib
```

## Creating a database and database user 

During the Postgres installation, an operating system user named `postgres` was created to correspond to the `postgres` PostgreSQL administrative user. You need to use this user `postgres` to perform administrative tasks. Use `sudo` to pass in the username `postgres` along with the `-u` option which runs the command as a user, instead of root. Log into the interactive Postgres session by writing the following:

```
sudo -u postgres psql
```

If you run the above code, a new shell script appears: `postgres=#`...

Now let's create a database and provide a name for it --`my_django`. 

`CREATE DATABASE my_django;`

Now let's create a user for this database. 

```
CREATE USER samuel WITH PASSWORD '2013';
```

Let's do some modifications that will speed up our database operations.

```
ALTER ROLE samuel SET client_encoding TO 'utf8';
```

Let's grant all priviledges to the user `samuel`.

```
GRANT ALL PRIVILEGES ON DATABASE my_django TO samuel;
```

As a sanity check to see a list of the existing databases and to confirm the newly created is one of them you can do this via: `\list`.

```
                              List of databases
   Name    |  Owner   | Encoding | Collate |  Ctype  |     Access privileges     
-----------+----------+----------+---------+---------+---------------------------
 my_django | postgres | UTF8     | C.UTF-8 | C.UTF-8 | =Tc/postgres             +
           |          |          |         |         | postgres=CTc/postgres    +
           |          |          |         |         | samuel=CTc/postgres
 myproject | postgres | UTF8     | C.UTF-8 | C.UTF-8 | =Tc/postgres             +
           |          |          |         |         | postgres=CTc/postgres    +
           |          |          |         |         | sammigachuhi=CTc/postgres
--snip--
```

You can now exist the shell session via: `\q`.


## Installing `psycopg2`

This package is used to connect Python to the Postgresql database.

```
pip install Django psycopg2
```

## Make migrations

To persist our changes to the database, register our migrations and execute them via `python3 manage.py makemigrations` and `python3 manage.py migrate` respectively.

## Configure settings 


```
DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }

    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'my_django',
        'USER': 'samuel',
        'PASSWORD': '2013',
        'HOST': 'localhost',
        'PORT': '',
    }
}
```


