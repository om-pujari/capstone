from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class EmailPhoneBackend:
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # Check if username is an email
            if '@' in username:
                user = User.objects.get(email=username)
            else:
                # Assume it's a phone number
                user = User.objects.get(phone_number=username)

            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None