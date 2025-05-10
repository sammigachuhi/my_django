from django.contrib import admin
from .models import Questionnaire

# Register your models here.
class QuestionnaireAdmin(admin.ModelAdmin):
    pass 

admin.site.register(Questionnaire, QuestionnaireAdmin)