from django.urls import path
from . import views

app_name = "clicker"
urlpatterns = [
   path("", views.index, name="index"),
   path("new-button/", views.new_button, name="new-button")
]

# REST API

urlpatterns += [
   path("handle-click/", views.handle_click, name="handle-click"),
]
