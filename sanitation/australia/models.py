from django.db import models
from datetime import date
from django.utils import timezone

# Create your models here.
class Researcher(models.Model):

    RESEARCHERS_LIST = {
        "Bwana_Waziri": "Bwana Waziri",
        "Samuel_Gachuhi": "Samuel Gachuhi",
        "Jane_Otieno": "Jane Otieno",
        "Janet_Awino": "Janet Awino",
        "William_Kinyanjui": "William Kinyanjui",
        "Johnson_Ngugi": "Johnson Ngugi"
    }

    researchers = models.CharField(choices=RESEARCHERS_LIST, default="Bwana_Waziri")

    def __str__(self):
        return self.researchers
    


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

    # RESEARCHERS_LIST = {
    #     "Bwana_Waziri": "Bwana Waziri",
    #     "Samuel_Gachuhi": "Samuel Gachuhi",
    #     "Jane_Otieno": "Jane Otieno",
    #     "Janet_Awino": "Janet Awino",
    #     "William_Kinyanjui": "William Kinyanjui",
    #     "Johnson_Ngugi": "Johnson Ngugi"
    # }

    survey_date = models.DateField(default=date.today)

    survey_time = models.TimeField(default=timezone.localtime)

    territory = models.CharField(
        choices=TERRITORY_CHOICES,
        default=WA
    )

    area = models.TextField()

    recorder = models.ForeignKey(Researcher, on_delete=models.CASCADE,)

    def __str__(self):
        return f"Date: {self.survey_date} Recorder: {self.recorder}"



    