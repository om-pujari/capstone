from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from Bike import models


# Create your views here.

class Home(ListView):
    template_name = 'home.html'
    model = models.Bike
    context_object_name = "bike_prod"
