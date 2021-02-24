from django.shortcuts import redirect, render
from .models import *
from django.views.decorators.http import require_http_methods
# Create your views here.

def index(request):
    return render(request, "pages/index.html", context={
        "buttons": list(Button.objects.all())
    })

@require_http_methods(["POST"])
def handle_click(request):
    body = request.POST
    btn = Button.objects.get(id=body["id"])
    if body["val"] == "like":
        btn.like()
    elif body["val"] == "dislike" and btn.count != 0:
        btn.dislike()
    btn.save()
    return redirect("clicker:index")
