from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from Bike.models import Bike,Maintenance
from .forms import UserUpdateForm, RegisterForm,CustomPasswordResetForm
from Query.models import Query
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from TestDrive.models import TestDrive
from django.contrib.auth import get_user_model,login

User = get_user_model()

class RegisterView(CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'User/register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        # Save the user
        user = form.save()

        # Get the first backend and use it
        from django.contrib.auth import get_backends
        backend = get_backends()[0]

        # Login with the backend
        login(self.request, user, backend=backend.__class__.__module__ + "." + backend.__class__.__name__)

        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        for field in form.fields:
            form.fields[field].widget.attrs.update({'class': 'form-control'})
        return form


class UserLoginView(LoginView):
    template_name = 'User/login.html'
    next_page = 'home'
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['username'].widget.attrs.update({'class': 'form-control'})
        form.fields['password'].widget.attrs.update({'class': 'form-control'})
        return form


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

@login_required
def user_profile(request):
    user = request.user
    maintenance_requests = Maintenance.objects.filter(user=user).exclude(status="Completed")
    queries = Query.objects.filter(user=user)  # Fetch user queries
    wishlist = user.wishlist.all()  # Fetch wishlist items
    test_drive_requests = TestDrive.objects.filter(user=user)

    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('User:profile')

    else:
        form = UserUpdateForm(instance=user)

    context = {
        'form': form,
        'queries': queries,
        'wishlist': wishlist,
        'maintenance_requests':maintenance_requests,
        'test_drive_requests':test_drive_requests,
    }
    return render(request, 'user/profile.html', context)




class CustomPasswordResetView(PasswordResetView):
    template_name = 'User/password_reset_form.html'
    email_template_name = 'User/password_reset_email.html'
    subject_template_name = 'User/password_reset_subject.txt'
    # Note: Using reverse_lazy with namespace
    success_url = reverse_lazy('User:password_reset_done')
    form_class = CustomPasswordResetForm