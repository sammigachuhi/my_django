
# Chapter 19 

We want to create some templates. In Django, a [template](https://docs.djangoproject.com/en/5.2/topics/templates/) contains the static part of the desired HTML output as well as some syntax that describes how a dynamic content will be inserted. 

We will create some templates for:

1. Our geolocations homepage.

2. Our geolocations questions 

3. A webmap for where each of our surveys took place 


## Create the `templates` folder

Within our `geolocations` app, create `templates` folder and within it create the `geolocations` folder. We use this naming convention of `app_name/templates/app_name` to avoid clashes if there were other apps that could have their own html templates with the same names. 

Within the `geolocations/templates/geolocations` directory, create an `index.html` file. So your templates structure will look like:

```
geolocations
├── apps.py
├── templates
│   └── geolocations
│       └── index.html

```

Within the `index.html` file, insert the below content.

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Geolocations app</title>
</head>
<body>
    <h1>We would like to survey you if you plan to be a GMO farmer!</h1>
    <embed src="https://sammigachuhi.github.io/pro-gmo-website/" type="text/html" width="1600px" height="800px">
</body>
</html>
```

This is a nested website that also hosts the Pro-GMO website from [here](https://sammigachuhi.github.io/pro-gmo-website/). We use the `<embed>` tag to embed the Pro-GMO website within our `index.html`. 

## Configuring the views

We aren't done yet. 

Go to your `geolocations/views.py` file. Change the home function from returning a simple HttpsResponse via `return HttpsResponse` to rendering a html page via the `render()` function. 


```
def home(request):
    return render(request, "geolocations/index.html", {})
```

Now, if you run `python3 manage.py runserver` and go to your local host `http://127.0.0.1:8000/`, you will see our homepage as below.


![New geolocations home page](images/new_geolocations_home_page.PNG)





