from django.http import HttpResponse
from django.shortcuts import render


def home(request: object) -> HttpResponse:
    #return HttpResponse("Hello,World! I'm Home")
    return render(request, 'home.html') #no need to specify the path to the templates folder
    #because we already did it in the settings.py file


def about(request: object) -> HttpResponse:
    #return HttpResponse("Hello,World! I'm About")
    return render(request, 'about.html', status=220) 