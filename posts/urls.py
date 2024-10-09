from django.urls import path
from . import views
from typing import List


app_name = 'posts'

urlpatterns:List[path] = [
    path(route='players/', view=views.renderizar_miVista, name='mi_vista'),
    path(route='lista/', view=views.post_lista, name='mi_lista'),
    path(route='<slug:slug>', view=views.post_pagina, name='pagina', ),

]
