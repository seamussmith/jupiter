import json
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from .models import *
from django.views.decorators.http import require_http_methods
import time
# Create your views here.

def index(request):
    return render(request, "pages/index.html", context={
        "buttons": list(reversed(Button.objects.all()))
    })

@require_http_methods(["POST"])
def handle_click(request):
    body = request.POST
    btn = Button.objects.get(id=body["id"])
    if body["val"] == "like":
        btn.like()
    elif body["val"] == "dislike" and btn.count != 0:
        btn.dislike()
    d = btn.to_dict()
    btn.save()
    return JsonResponse(d)

SPAM_DELAY = 20
@require_http_methods(["POST"])
def new_button(request):
    body = request.POST
    curr_time = time.time()
    if request.session.get("last_submit") is not None:
        last_time = request.session["last_submit"]
        delta = curr_time - last_time
        if delta < SPAM_DELAY:
            return HttpResponse(f"Dont spam! Please wait {round(SPAM_DELAY - delta)} more seconds!", status=429)
    request.session["last_submit"] = time.time()
    btn = Button.new(body["text"])
    btn.save()
    return redirect("clicker:index")
