from django.shortcuts import render
from .forms import InternshipForm, StudentPlacementForm


def create_placement(request):
    context = {}
    context['form'] = StudentPlacementForm()
    return render(request, 'placements/placementReg.html', context)


def create_internship(request):
    context = {}
    context['form'] = InternshipForm()
    return render(request, 'placements/internshipReg.html', context)

