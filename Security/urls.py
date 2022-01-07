# Django
from django.urls import path

# Enpoints
from Security.endpoints.resources_enpoints import find_resources, save_resource
from Security.endpoints.auth_endpoints import AuthEnpoints
from Security.endpoints.profile_endpoints import ProfileApis

urlpatterns = [
    # Resources
    path('v1/security/resources/', find_resources ),
    path('v1/security/resources/created', save_resource ),

    # Profiles
    path('v1/security/profile/', ProfileApis.as_view() ),

    # Authentication
    path('v1/security/login', AuthEnpoints.as_view() )



]
