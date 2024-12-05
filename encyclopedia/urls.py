from django.urls import path
from . import views

app_name = "main"
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki", views.index, name="index"),
    path("search", views.search, name="search"),
    path("wiki/<str:name>", views.title, name="title"),
]
