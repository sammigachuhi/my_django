# Chapter 3

## Add the app 

We add apps inside the `settings.py` file under your project folder, in this case `sanitation`.

To include an app in your project, you need to reference to its configuration class at the beginning of the `INSTALLED_APPS` list in `settings` file.

This enables Django know that there is a new app in town.

In order to display something for our app, we have to create a view.

## Create a view

A view in Django is a collection of functions or classes inside the `views.py` file in an app's directory. Each function or class handles the logic that the app processes each time the user visits a different URL.

The `views.py` file is found under your app's directory, which is `australia` in this case.

Inside the `australia/views.py` file, insert the following code.

```
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "australia/home.html", {})
```

In this piece of code, you define a **view function** named `home()`. When you call this function, it'll render an HTML file named `home.html`.

**NB**: A view function takes at least one argument, request. The request object is created whenever a page loads, and it contains metadata about the page request.

Now that you’ve created the view function, you need to create the HTML template to display to the user. The render() function looks for HTML templates inside a directory called templates/ in your app directory. Since templates of different apps can have the same names, it’s also best practice to add a subdirectory with the app’s name inside the templates/ directory.

Create the templates/ directory, a subdirectory named pages/, and subsequently a file named `home.html` inside it.

Once you’ve created the template folders and home.html, open the HTML file in your editor and add the following lines of code:

`<h1>Australia, welcome</h1>`

For clarity, here is the directory structure of our `australia` app.

```
australia
├── apps.py
├── templates
│   └── australia
│       └── home.html
├── views.py

--snip--
```

Now that you’ve created the template that your home() view function expects, you need to tell Django when to serve the view. For this, you need to create a new route to the project.
