from django.db import models

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

    