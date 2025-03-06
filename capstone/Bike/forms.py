from django import forms
from .models import Maintenance, ServiceType,Bike,Comparison

class MaintenanceForm(forms.ModelForm):
    service_type = forms.ModelChoiceField(
        queryset=ServiceType.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})  # Dropdown for service type
    )
    service_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})  # Date picker
    )
    bike = forms.ModelChoiceField(
        queryset=Bike.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})  # Dropdown for bike selection
    )
    comments = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        required=False
    )
    class Meta:
        model = Maintenance
        fields = ['bike', 'service_type','service_date']  # Add 'bike' selection


class ComparisonForm(forms.Form):
    bike_one = forms.ModelChoiceField(
        queryset=Bike.objects.all(),
        empty_label="Choose first bike",
        widget=forms.Select(attrs={'class': 'form-select'}),
        required=False  # Allow optional selection
    )
    bike_two = forms.ModelChoiceField(
        queryset=Bike.objects.all(),
        empty_label="Choose second bike",
        widget=forms.Select(attrs={'class': 'form-select'}),
        required=False  # Allow optional selection
    )

    def clean(self):
        cleaned_data = super().clean()
        bike_one = cleaned_data.get('bike_one')
        bike_two = cleaned_data.get('bike_two')

        # Ensure two different bikes are selected
        if bike_one and bike_two and bike_one == bike_two:
            raise forms.ValidationError("Please select two different bikes.")

        return cleaned_data
