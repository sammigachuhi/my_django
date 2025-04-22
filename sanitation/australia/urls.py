from django.urls import path 
from australia import views

urlpatterns = [
    path("", views.home, name="home"),
    path("sanitation", views.sanitation, name="sanitation"),
]

