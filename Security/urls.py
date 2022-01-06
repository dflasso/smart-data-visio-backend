# Django
from django.urls import path

# Enpoints
from Security.endpoints.resources_enpoints import find_resources


urlpatterns = [
    path('resources/', find_resources )
]
