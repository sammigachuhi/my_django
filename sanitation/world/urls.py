from django.urls import path  
from world import views 


urlpatterns = [
    path("dysentry", views.dysentry, name="dysentry"),
]













