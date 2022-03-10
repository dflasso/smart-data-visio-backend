
# Django rest framework
from rest_framework.routers import DefaultRouter

# Enpoints
from analytics.endpoints import SuggestionEndpoints

router = DefaultRouter()
# ophthalmological test
router.register(r'v1/tests/ophthalmological/suggestion', SuggestionEndpoints, basename='ophthalmological_suggestion')


urlpatterns = router.urls
