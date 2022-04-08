from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("display/", views.random_entry, name="displayrandom"),
    path("display/", views.search, name="search"),
]
