from django.urls import path
from . import views

app_name = "main"
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki", views.index, name="index"),
    path("search", views.search, name="search"),
    path("create", views.create, name="create"),
    path("add", views.add, name="add"),
    path("edit", views.edit, name="edit"),
    path("random", views.random, name="random"),
    path("error", views.error, name="error"),
    path("wiki/<str:name>", views.title, name="title")
]
