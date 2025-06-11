
# Chapter 21 

## Prerequisites

This chapter shall detail how to host your geodjango application on Render. It may not be the ideal, but hosting will follow one or more of the following steps.

First, install the `gunicon`, `whitenoise` and `psycopg2-binary` packages. 

```
pip install gunicorn whitenoise psycopg2-binary
```

Secondly, update your `requirements.txt` file as this is what Render will use to host your app.

```
pip freeze > requirements.txt
```

## Configure `settings.py`

At the very top, ensure the following packages have been called.

```
import os
import dj_database_url
```

Then, in your `DATABASES` variable, use the following `default` settings. Uncomment any other `default` variable you have within `DATABASES` to use this one.

```
'default': dj_database_url.config(
        default='sqlite:///db.sqlite3', # Fallback to SQLite for local development if DATABASE_URL isn't set
        conn_max_age=600,
        # engine='django.contrib.gis.db.backends.postgis', # Specify PostGIS engine
        # Optionally, set this if you want to use a specific URL from env, 
        # though dj_database_url usually handles this well
        # conn_health_checks=True, 
    )

```

You may have questions, as why the former that we created that was successful on our laptop now has to be changed to this one. It is what partially worked compared to the former that just couldn't start up our server.

Within your `settings.py` file, ensure that your `ALLOWED_HOSTS` variable is set to `ALLOWED_HOSTS = ['*']`,

At the bottom of your `settings.py` file, add the following:

```
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
```



## Run migrations

We want the database to get updated with the latest changes. Therefore, first run `python3 manage.py makemigrations` and thereafter, `python3 manage.py migrate`.

Thereafter push your Django to Gihub.

## Create postgres on Render

Geodjango requires Postgres to run and because of that, we will create a Postgres instance on Render.

Inside Render, click on *New > Postgres*. 

Provide a unique **Name**.

Provide **Database** name. 

Select the **Region** that will host your Postgres instance. 

Leave **PostgreSQL** version at its default. 

Select **Free** under **Instance Type** and click **Create Database**. Wait for your database to be created.

## Create Django web service on Render 

On Render, create *New > Web Service*. 

Create a unique **Name** for your web service

Select a **Region** that will host your web service.

Leave **Instance Type** as free. 

Next to **Build Command**, we shall provide our `requirements.txt` file. Use these values: `pip install -r requirements.txt`.

Under **Start Command**, use this: `python manage.py runserver 0.0.0.0:8000`. 

For the **Environment Variables**, the *Key* and *Value* parameters will be as follows, respectively.

PYTHON_VERSION              3.10.12

DATABASE_URL                <your-postgres-internal-or-external-database-url>


For the `DATABASE_URL`, we shall use either the internal or external database url for the Postgres instance we created earlier. These values can be found in the *Info* tab of your Postgres instance on render.

Once satisfied, go ahead and deploy your django web service.

At the end of the deployment, a link will be provided at the very top. Here is our Pro GMO website. Unfortunately, the other hosted webpages showing the results of our questions couldn't be displayed. 

![Pro GMO website](images/pro_gmo_website.PNG)

