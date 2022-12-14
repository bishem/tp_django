from tempfile import template
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class AcceuilView(TemplateView):
  template_name = "acceuil.html"
