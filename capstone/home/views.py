from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class Home(TemplateView):
    template_name = 'home.html'


class Visit(TemplateView):
    template_name = 'visit-us.html'