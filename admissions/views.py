from django.shortcuts import render, redirect
from .forms import StudentForm, EmployeeForm, AdmissionSecForm
from .models import Student, Employee, AdmissionSection
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.


def create_student(request):
    context = {}
    context['form'] = StudentForm()
    return render(request, 'admissions/studentReg.html', context)


def get_stdData(request):
    query = Student.objects.all()
    context = {"query": query}
    return render(request, 'admissions/stdDisplay.html', context)


def save_student(request):
    std_data = StudentForm(request.POST)
    if std_data.is_valid():
        std_data.save()
    return HttpResponseRedirect(reverse('stddisplay'))


def create_employee(request):
    context = {}
    context['form'] = EmployeeForm()
    return render(request, 'admissions/employeeReg.html', context)


def get_emp_data(request):
    query = Employee.objects.all()
    context = {"query": query}
    return render(request, 'admissions/empDisplay.html', context)


def create_admission(request):
    context = {}
    context['form'] = AdmissionSecForm
    return render(request, 'admissions/admissionSecReg.html', context)


def get_sec_details(request):
    query = AdmissionSection.objects.all()
    context = {"query": query}
    return render(request, 'admissions/adminSecDisplay.html', context)

