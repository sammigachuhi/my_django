from django.contrib import admin
from .models import Researcher
from .models import Questionnaire

# Register your models here.
class ResearchersAdmin(admin.ModelAdmin):

    fields = ("researchers",)


class QuestionnaireAdmin(admin.ModelAdmin):
    # pass 
    # readonly_fields = ("survey_date", "survey_time",)
    fields = ("survey_date", "survey_time", "territory", "area", "recorder",)


admin.site.register(Researcher, ResearchersAdmin)
admin.site.register(Questionnaire, QuestionnaireAdmin)