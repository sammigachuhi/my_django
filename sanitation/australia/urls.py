from django.urls import path 
from australia import views

urlpatterns = [
    path("", views.home, name="home"),
    path("sanitation", views.sanitation, name="sanitation"),
    path("questionnaires", views.questionnaire_index, name="questionnaires"),
    path("questionnaires/<int:pk>/", views.questionnaire_detail, name="questionnaire_detail"),
]

