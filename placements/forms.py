from django import forms
from placements.models import StudentPlacements, Internship


class StudentPlacementForm(forms.ModelForm):
    class Meta:
        model = StudentPlacements
        fields = '__all__'
        exclude = ['createdOn']


class InternshipForm(forms.ModelForm):
    class Meta:
        model = Internship
        fields ='__all__'
        exclude = ['createdOn']

