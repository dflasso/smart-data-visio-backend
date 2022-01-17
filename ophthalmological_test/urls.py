# Django
from django.urls import path, include

# Django rest framework
from rest_framework.routers import DefaultRouter

# Enpoints
from ophthalmological_test.endpoints import OphthalmologicalTestEndpoints

router = DefaultRouter()
# ophthalmological test
router.register(r'v1/tests/ophthalmological', OphthalmologicalTestEndpoints, basename='ophthalmological_test')


urlpatterns = router.urls
