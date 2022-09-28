from django.urls import path
from .views import create_student, create_employee, create_admission, get_stdData, get_emp_data, get_sec_details, \
    save_student


urlpatterns = [
    path('stdreg', create_student, name = 'stdreg'),
    path('empreg', create_employee, name = 'empreg'),
    path('admissionSecReg', create_admission, name='admissionSecReg'),
    path('stdDisplay', get_stdData, name='stddisplay'),
    path('empDisplay', get_emp_data, name='empDisplay'),
    path('secDisplay', get_sec_details, name='secDisplay'),
    path('saveStdData', save_student, name='saveStdData')
]

