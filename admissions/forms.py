from django import forms
from admissions.models import Student, Employee, AdmissionSection


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        exclude = ['createdOn']


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        exclude = ['createdOn']


class AdmissionSecForm(forms.ModelForm):
    class Meta:
        model = AdmissionSection
        fields = '__all__'
