from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Post


def renderizar_miVista(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name='players.html',) 


# Create your views here.
def posts_List(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name='posts/index.html', )


def post_lista(request: HttpRequest) -> HttpResponse:
    posts = Post.objects.all().order_by('-date')
    return render(request=request, template_name='posts/post_list.html', context={'posts': posts})


def post_pagina(request:HttpRequest, slug:str) -> HttpResponse:
    posts = Post.objects.get(slug=slug)
    return render(request=request, template_name='posts/post_pagina.html', context={'post': posts})

