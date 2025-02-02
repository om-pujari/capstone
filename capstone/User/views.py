from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from Bike.models import Bike

class RegisterView(CreateView):
    model = User
    template_name = 'User/register.html'
    success_url = reverse_lazy('home')
    fields = ['name', 'email', 'phone_number', 'password']

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        # Ensure user permissions are not set here
        user.is_staff = False  # Explicitly not staff
        user.is_superuser = False  # Explicitly not superuser
        user.save()
        return super().form_valid(form)

class UserLoginView(LoginView):
    template_name = 'User/login.html'
    next_page = 'home'


class UserLogoutView(LogoutView):
    next_page = 'home'


@login_required
def toggle_wishlist(request, bike_id):
    """Add or remove a bike from the user's wishlist."""
    bike = get_object_or_404(Bike,id=bike_id)
    if bike in request.user.wishlist.all():
        request.user.wishlist.remove(bike)
    else:
        request.user.wishlist.add(bike)
    return redirect('Bikes:detail', pk=bike.id)