# Chapter 01

## Creating virtual environment

We will first start by creating a virtual environment. A virtual environment isolates your project dependencies to within the project you are working in so that it doesn't affect other projects, even if they use different versions of your dependencies, if at all.

```
python3 -m venv venv
```

## Activating virtual environment 

Now let's activate the virtual environment we created. You have to activate your virtual environment so that it can encapsulate the dependencies you will work with. If you install if it is not activated, it is like dropping bombs outside the military training zone.

```
source venv/bin/activate
```

## Installing django 

Now that we have activated a virtual environment, we can now install django which will be imprisoned inside that virtual environment. Any other project we create can use a different version of django without it being affected by the version we input here.

```
pip install django
```

## Storing requirements

Let's create a file store every package we will use in this journey. A short pen is better than a long memory.

```
pip freeze > requirements.txt
```

## Create project 

Now let's create a django project. But first, it is important to understand two concepts, a project and an app in the context of django.

Django project - is a high-level unit of organization that contains logic that governs your whole web application. Each project can contain multiple apps.

Django app - is a lower-level unit of your web application. You can have zero to many apps in a project, and you’ll usually have at least one app.

Now let's create our project!

```
django-admin startproject sanitation
```

## Create app 

We want to duplicate the interactive dashboard showing all Australia's public toilets in our django app. At first we wanted a more descriptive name, `australia-toilets` but python would here none of that. Perhaps it's because we had a hyphen (-) in our app name?

```
python3 manage.py startapp australia-toilets
```

The above app creation using `australia-toilets` resulted in the following error.

```
CommandError: 'australia-toilets' is not a valid app name. Please make sure the name is a valid identifier.
```

However, we ate humble pie and decided to go with `australia` instead. Not that we are mocking the country. The fact that I am using Australia here and in the dashboard is testament enough it is a standard when it comes to proper sanitation countrywide. So we go simple.

```
python3 manage.py startapp australia
```

## Peek inside the project folder

So this is how our directory looks like:

```
sanitation
├── manage.py
├── australia
│   ├── apps.py
│   ├── views.py
│   ├── migrations
│   │   └── __init__.py
│   ├── __init__.py
│   ├── admin.py
│   ├── tests.py
│   └── models.py
└── sanitation
    ├── wsgi.py
    ├── settings.py
    ├── __init__.py
    ├── asgi.py
    ├── urls.py
    └── __pycache__
        ├── __init__.cpython-310.pyc
        └── settings.cpython-310.pyc

4 directories, 15 files
```

Inside our `sanitation` project, this is how the directory structure looks like.

```
sanitation
    ├── wsgi.py
    ├── settings.py
    ├── __init__.py
    ├── asgi.py
    ├── urls.py
    └── __pycache__
        ├── __init__.cpython-310.pyc
        └── settings.cpython-310.pyc

```