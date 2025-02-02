from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView,CreateView
from .forms import QueryForm
from .models import Query
from django.urls import reverse_lazy
# Create your views here.


class Query_Form(LoginRequiredMixin, CreateView):
    model = Query
    template_name = "Query/query_form.html"
    form_class = QueryForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()  # Save the form data to the database
        return super().form_valid(form)