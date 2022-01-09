# Django
from django.urls import path, include

# Django rest framework
from rest_framework.routers import DefaultRouter

# Enpoints
from classic_test.endpoints.lang_endpoint import LangEnpoints
from classic_test.endpoints.lang_results_endpoints import LangResultsEnpoints

router = DefaultRouter()
router.register(r'v1/visual-test/classic/lang', LangEnpoints, basename='lang')
router.register(r'v1/visual-test/classic/lang/results', LangResultsEnpoints, basename='lang_results')

urlpatterns = router.urls
