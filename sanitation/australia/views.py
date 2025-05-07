from django.shortcuts import render
from australia.models import Questionnaire 

# Create your views here.
def home(request):
    return render(request, "australia/home.html", {})

def sanitation(request):
    return render(request, "australia/sanitation.html", {})

def questionnaire_index(request):
    questionnaires = Questionnaire.objects.all()
    context = {
        "questionnaires": questionnaires
    }
    return render(request, "australia/questionnaires.html", context)


def questionnaire_detail(request, pk):
    questionnaire = Questionnaire.objects.get(pk=pk)
    context = {
        "questionnaire": questionnaire
    }
    return render(request, "australia/questionnaire_detail.html", context)






