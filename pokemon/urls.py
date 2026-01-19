from django.urls import path
from . import views

urlpatterns = [
    path("list", views.pokemon_list),
    path("", views.pokemon_create),
    path("delete", views.pokemon_delete),
]
