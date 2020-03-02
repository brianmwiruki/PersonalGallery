from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import Picture
import datetime as dt

# Create your views here.

def picture(request,picture_id):

    try: 
        picture = Picture.objects.get(id = picture_id)
    except DoesNotExist:
        raise Http404()
    return render(request, "pictures.html", {"picture": picture})