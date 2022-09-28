from django.shortcuts import render
from .forms import StudentForm, FacultyForm, DepartmentForm


def create_student(request):
    context = {}
    context['form'] = StudentForm()
    return render(request, 'departments/studentReg.html', context)


def create_faculty(request):
    context = {}
    context['form'] = FacultyForm()
    return render(request, 'departments/facultyReg.html', context)


def create_department(request):
    context = {}
    context['form'] = DepartmentForm()
    return render(request, 'departments/departmentReg.html', context)





