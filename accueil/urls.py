from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path("", RedirectView.as_view(url="hello"), name="acceuil"),
    path("hello/", views.AcceuilView.as_view(), name="hello"),
    path("sum/", views.sum_view, name="sum"),
    path("sum_bis/", views.sum_bis_view, name="sum_bis"),
]
