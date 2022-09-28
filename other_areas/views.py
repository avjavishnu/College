from django.shortcuts import render
from other_areas.forms import DriverForm


def create_driver(request):
    context = {}
    context['form'] = DriverForm()
    return render(request, 'other_areas/driverReg.html', context)

