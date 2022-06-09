from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("aryan", views.aryan,name = "aryan"),
    path("<str:name>", views.greet, name="greet")
]