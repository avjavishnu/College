from django.urls import path
from .views import create_internship, create_placement


urlpatterns = [
    path('placementreg', create_placement, name='placementreg'),
    path('internshipreg', create_internship, name='internshipreg')
]
