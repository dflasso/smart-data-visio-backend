
# Django rest framework
from rest_framework.routers import DefaultRouter

# Enpoints
from virtual_task.endpoints import ResultsVirtualTaskEndpoints

router = DefaultRouter()
# ophthalmological test
router.register(r'v1/tests/ophthalmological/virtual_task/results', ResultsVirtualTaskEndpoints, basename='results_virtual_test')


urlpatterns = router.urls
