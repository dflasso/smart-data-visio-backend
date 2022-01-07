# Django
from django.urls import path

# Endpoints
from patients.endpoints import PatientsApis

urlpatterns = [
    # 
    path('v1/patients/', PatientsApis.as_view() ),
]