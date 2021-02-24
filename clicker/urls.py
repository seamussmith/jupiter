from django.urls import path
from . import views

app_name = "clicker"
urlpatterns = [
   path("", views.index, name="index"),
   path("handle-click/", views.handle_click, name="handle-click")
]
