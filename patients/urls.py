# Django rest framework
from rest_framework.routers import DefaultRouter

# Endpoints
from patients.endpoints import PatientsApis, PatientsPagination


router = DefaultRouter()
# ophthalmological test
router.register(r'v1/patients', PatientsApis, basename='patients')
router.register(r'v1.1/patients', PatientsPagination, basename='patients')
router.register(r'v1/medical_history', PatientsApis, basename='medical_history')


urlpatterns = router.urls