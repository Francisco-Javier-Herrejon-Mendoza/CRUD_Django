from django.contrib import admin
from django.urls import path
import crud.views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', crud.views.home, name="home"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)