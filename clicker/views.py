from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    return render(request, "pages/index.html", context={
        "buttons": list(Button.objects.all())
    })
