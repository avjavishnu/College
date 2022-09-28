from django.urls import path
from .views import create_student, create_faculty, create_department

urlpatterns = [
    path('stdreg', create_student, name='stdreg'),
    path('facultyreg', create_faculty, name='facultyreg'),
    path('deptreg', create_department, name='deptreg')
]