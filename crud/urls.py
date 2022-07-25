from django.contrib import admin
from django.urls import path
import crud.views

urlpatterns = [
    path('', crud.views.home, name="home"),
]