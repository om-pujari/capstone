from django.shortcuts import render
from django.views.generic import ListView,DetailView
from . import models
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, View
from django.shortcuts import redirect
from .models import Bike
from TestDrive.models import TestDrive
# Create your views here.
class Bike_List(ListView):
    context_object_name = "prod"
    model = models.Bike


class Bike_Detail(DetailView):
    context_object_name = 'dets'
    model = models.Bike


class BookTestDriveView(LoginRequiredMixin, View):
    def post(self, request, pk):
        bike = Bike.objects.get(pk=pk)
        TestDrive.objects.create(
            user=request.user,
            bike=bike,
            test_drive_date=request.POST.get('test_drive_date')
        )
        return redirect('Bikes:detail', pk=pk)