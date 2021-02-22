from django.urls import path
from . import views

app_name = "clicker"
urlpatterns = [
   path("", views.index) 
]
