from django import forms
from departments.models import Student, Department, Faculty, Lab


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        exclude = ['createdOn']


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'
        exclude = ['createdOn']


class FacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = '__all__'
        exclude = ['createdOn']


class LabForm(forms.ModelForm):
    class Meta:
        model = Lab
        fields = '__all__'
        exclude = ['createdOn']