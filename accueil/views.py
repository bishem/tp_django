from tempfile import template
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class AcceuilView(TemplateView):
  template_name = "hello.html"


def sum_view(request):
  if request.POST:

    first: str = request.POST["first"]
    second: str = request.POST["second"]

    result: float

    if first.isalnum() and second.isalnum():
      result = float(first) + float(second)

      return render(
          request,
          template_name="sum.html",
          context={"sum": result})

  return render(request, template_name="sum.html")


def sum_bis_view(request):
  return render(request, template_name="sum_bis.html")
