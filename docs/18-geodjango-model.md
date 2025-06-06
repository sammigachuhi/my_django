
# Chapter 18 

## Model outline

Let's assume we are researchers who are going to research on the relationship between age and type of crops grown, and where in the country (represented by counties).


We want to design a form that will collect responses to the following questions:

1. Researchers - a multi-select question that inserts the names of all researchers involved in the project.

2. Recorder - the person conducting the survey.

3. Responder name - the person responding to the survey (optional)

4. Location - the geographic coordinates of where the survey is being carried out. This field will collect the coordinates as a point layer.

5. Age - this is the age of the respondent 

6. Crops - a multi-select dropdown question that allows the recorder to select the crops grown

7. Image - an image of the respondent's farm (optional).

8. Comments - a textfield that allows the recorder to add any other information not collected above but that provides more context. 


## Designing the model 

Let's create our first model that will capture the name of the researcher.

At the very top, import the models.

```
from django.db import models
from django.contrib.gis.db import models
```

Now here is the class to capture our researchers' names.

```
class Researcher(models.Model):

    full_name = models.CharField(max_length=50)

    def __str__(self):
        return self.full_name

```

Now add the following class that will capture the rest of the questions 2 to 8 above. Notice that the `Recorder` field is related to the `Researchers` field via a many-to-one relationship as exemplified by the `ForeignKey` field. 

```
class Question(models.Model):

    CROPS = {
        "maize": "Maize",
        "wheat": "Wheat",
        "rice": "Rice",
        "potatoes": "Potatoes",
        "green_grams": "Green grams",
        "beans": "Beans",
        "sugarcane": "Sugarcane",
        "arrowroots": "Arrow roots"
    }

    recorder = models.ForeignKey(Researcher, on_delete=models.CASCADE)
    names = models.CharField(max_length=100)
    location = models.PointField()
    age = models.IntegerField()
    crops = models.CharField(
        choices=CROPS,
        default="potatoes"
    )

    image = models.ImageField(upload_to='images/')

    comments = models.TextField()

    def __str__(self):
        return self.recorder, self.names, self.location, self.age, self.crops

```

Since we also want to capture images, we shall add two new variable in the `settings.py` file.

```
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

```

Also, we shall add a new addition to the `agriculture/urls.py` file. At the very top, import the `include`, `settings`, and `static` packages.

```
from django.contrib import admin
from django.urls import path, include 
from django.conf import settings
from django.conf.urls.static import static
```

Then add the static images to the `urlpatterns` variable.

```
urlpatterns = [
    path('admin/', admin.site.urls),
    # path("", include("geolocations.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

```

In the `geolocations/admin.py` file, we shall import some new tools.

Here we go.

```
from django.contrib import admin
from .models import Researcher, Question
# from django.contrib.gis.admin import OSMGeoAdmin
from django.contrib.gis.admin import GISModelAdmin

```

Let's also register our models.

```
@admin.register(Researcher)
class ResearcherAdmin(GISModelAdmin):
    list_display = ('full_name',)

@admin.register(Question)
class QuestionAdmin(GISModelAdmin):
    list_display = ('recorder', 'names', 'location', 'age', 'crops',)

```


