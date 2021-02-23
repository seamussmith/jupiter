from django.urls import path
from . import views

app_name = "rootapp"
urlpatterns = [
   path("", views.index, name="index")
]
