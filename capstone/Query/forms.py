from django import forms
from .models import Query

class QueryForm(forms.ModelForm):
    class Meta:
        model = Query
        fields = ['subject','message']
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control'}),  # Add form-control
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),  # Add form-control
        }
