from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("accueil.urls")),
    path("__reload__/", include("django_browser_reload.urls")),
]
