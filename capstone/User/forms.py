from django import forms
from .models import User

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email','name','phone_number']
