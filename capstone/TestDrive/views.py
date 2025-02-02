from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView
from .models import TestDrive


#views written for forms can delete Templates if wanna remove the following view
class Test(LoginRequiredMixin,FormView):
    model = TestDrive

    template_name = 'TestDrive/TestDrive.html'

