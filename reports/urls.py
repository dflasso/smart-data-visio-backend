
# Django rest framework
from rest_framework.routers import DefaultRouter

# Enpoints
from reports.endpoints import ReportSugestionEndpoints

router = DefaultRouter()
# ophthalmological test
router.register(r'v1/tests/ophthalmological/reports/suggestion', ReportSugestionEndpoints, basename='reports_suggestion')


urlpatterns = router.urls
