# Chapter 09 

## What is a model in Django?

A [Django model](https://www.geeksforgeeks.org/django-models/) is the built-in feature that Django uses to create tables, their fields and various constraints. In short, a Django model is the SQL Database one uses with Django. 

The basics of a model include: 

* Each model is a Python class that subclasses django.db.models.Model 

* Each attribute of the model represents a database field. 


## How to create models in Django?

In Django, models are defined inside a `models.py` script. 

We want to start simple. We want to assume that we want to create a database that for starters, captures the following information:

* survey_date - the date at which the survey was undertaken 

* survey_time - the time at which the survey was undertaken 

* territory - the administrative region at which the survey was undertaken 

* area - the state, town or neighbourhood the survey was carried out. Let's keep it very simple 


## Creating the class 

Models in Django are created under classes. We will create a class called `Questionnaire` which we shall use to create the model we want. 

```
# Create your models here.
class Questionnaire(models.Model):
```

We would like our first field to have a dropdown of the Australian territories. Therefore, within the `Questionnaire` class we create a list of constants:

```
class Questionnaire(models.Model):

    WA = "Western_Australia"
    NT = "Northern_Territory"
    QD = "Queensland"
    SA = "Southern_Australia"
    NSW = "New_South_Wales"
    TA = "Tasmania"

```

Now, let's create our proper territories list:

```
class Questionnaire(models.Model):

    WA = "Western_Australia"
    NT = "Northern_Territory"
    QD = "Queensland"
    SA = "Southern_Australia"
    NSW = "New_South_Wales"
    TA = "Tasmania"

    TERRITORY_CHOICES = [
        (WA, "Western Australia"),
        (NT, "Northern Territory"),
        (QD, "Queensland"),
        (SA, "Southern Australia"),
        (NSW, "New South Wales"),
        (TA, "Tasmania")
    ]

```

Why did we start with the list of constants. This is because we want the choices to be those that can be referenced in case we import the model inside another class. For example, `Questionnaire.WA` will work anywhere that the `Questionnaire` class has been imported. 

Now let's create the `territory` field which will contain our territory choices. 

```
    territory = models.CharField(
        choices=TERRITORY_CHOICES,
        default=WA
    )
```


Note that the `choices` parameter references the lists referenced by `TERRITORY_CHOICES`. 

Let's add a textfield in which the respondent will manually type out the area that they reside in.

```
area = models.TextField()

```

Just before the `territory` field, let's add `survey_date` and `survey_time` fields. We shall set the `auto_add_now` parameter to `True` so that the model automatically captures the current day and time respectively. So here is our `Questionnaire` class so far.

```
# Create your models here.
class Questionnaire(models.Model):

    WA = "Western_Australia"
    NT = "Northern_Territory"
    QD = "Queensland"
    SA = "Southern_Australia"
    NSW = "New_South_Wales"
    TA = "Tasmania"

    TERRITORY_CHOICES = [
        (WA, "Western Australia"),
        (NT, "Northern Territory"),
        (QD, "Queensland"),
        (SA, "Southern Australia"),
        (NSW, "New South Wales"),
        (TA, "Tasmania")
    ]

    survey_date = models.DateField(auto_now_add=True)

    survey_time = models.TimeField(auto_now_add=True)

    territory = models.CharField(
        choices=TERRITORY_CHOICES,
        default=WA
    )

    area = models.TextField()

    

```

