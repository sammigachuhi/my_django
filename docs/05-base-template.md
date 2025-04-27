# Chapter 5

## Beautifying our app

Remember the 'Australia, welcome' page? We want to make it prettier by using bootstrap. Think of bootstrap as that extra layer of makeup or foundation that a pretty girl applies before going out. [Bootstrap](https://getbootstrap.com/) is a front-end toolkit that is used to improve a webpage's look and feel.

Now, let's incorporate bootstrap into our app.

## Creating a `base.html` file

Create a directory named `templates/` in the `sanitation/` folder. Inside this new directory, create a file named `base.html`.

As you saw previously, each Django project can consist of multiple apps that handle separate logic, and each app contains its own `templates/` directory to store HTML templates related to the application. For templates that the whole project shares, it’s a good idea to create a `templates/` directory in the root directory. That's why we are creating the `templates/` directory inside our `sanitation` project directory.

Instead of having to import Bootstrap styles into every app, you can create a template or set of templates that all the apps share. As long as Django knows to look for templates in this new shared directory, it can save a lot of repeated styles.

## Adding bootstrap

Inside base.html, add the following lines of code:

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %} Australia public toilets {% endblock title %}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.5/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-SgOJa3DmI69IUzQ2PVdRZhwQ+dy64/BUtbMJw1MZ8t5HZApcHrRKUc4W0kG879m7" crossorigin="anonymous">
</head>
<body class="container">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.5/dist/js/bootstrap.bundle.min.js" integrity="sha384-k6d4wzSIapyDyv1kpU366/PK5hCdSbCRGRCMv+eplOQJWyd1fbcAu9OCUj5zNLiq" crossorigin="anonymous"></script>
    {% block base_content %} 
    
    {% endblock base_content %}
</body>
</html>

```

With the code above, you create the skeleton of a valid HTML document.

We add the bootstrap link to the `link` and `script` tags. The bootstrap link within the `link` tag of our html `<head>` is responsible for creating the bootstrap CSS while the `script` tag in the `body` section enables the JavaScript bundle for positioning dropdowns, popovers and tooltips.


## Jinja templates 

Another interesting bit in the `base.html` parent template is the use of `{% block %}` template tags in the `title` tag and `body` section. With this template tag, you can define content blocks that you can use or override in child templates that extend the parent template. That is, these template tags will enable you to replicate the styling in the base template to other apps.

To see this inheritance in action, you need to adjust the home.html template:

```
{% extends "base.html" %}

{% block base_content %}

    <h1>Australia, welcome</h1>

{% endblock base_content %}

```

To extend a parent template, you must use the `{% extends %}` tag at the beginning of a child template.

Note that you are only overriding the `base_content` block and not the `title` block. 

Before you can see the inheritance and the new styled application in action, you need to tell your Django example project that `base.html` exists. The default settings register `templates/` directories in each app, but not in the root directory itself. In `sanitation/settings.py`, update `TEMPLATES` with the base templates' path:

```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / "templates/",
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

```

## The bootstrapped page

You’ve already defined the constant `BASE_DIR` in `settings.py`, and it points to your project’s root directory. Next, you join the path with the forward slash operator (/) from pathlib to point to the templates/ directory and add it to the "DIRS" list.

When you rerun `python3 manage.py runserver` you can see that the home page has a slightly different styling.

Here, you have the *Australia, welcome* message that you defined in `home.html` as well as the *Australia public toilets* title that you set in `base.html`. That means that the template inheritance works!

Whenever you want create templates or import scripts that you intend to use in all of your Django apps inside a project, you can add them to this project-level directory and extend them inside your app templates.

![](./images/bootstrapped_page.png)





