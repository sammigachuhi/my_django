from django.db import models
from datetime import date
from django.utils import timezone

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

    survey_date = models.DateField(default=date.today)

    survey_time = models.TimeField(default=timezone.localtime)

    territory = models.CharField(
        choices=TERRITORY_CHOICES,
        default=WA
    )

    area = models.TextField()

    