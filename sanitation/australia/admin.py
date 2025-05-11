from django.contrib import admin
from .models import Questionnaire

# Register your models here.
class QuestionnaireAdmin(admin.ModelAdmin):
    # pass 
    # readonly_fields = ("survey_date", "survey_time",)
    fields = ("survey_date", "survey_time", "territory", "area",)

admin.site.register(Questionnaire, QuestionnaireAdmin)