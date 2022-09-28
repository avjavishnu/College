from django import forms
from other_areas.models import Driver


class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = '__all__'
        exclude = ['createdOn']
