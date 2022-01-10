# Django
from django.urls import path, include

# Django rest framework
from rest_framework.routers import DefaultRouter

# Enpoints
from classic_test.endpoints import IshiharaEndpoints, LangEnpoints, LangResultsEnpoints

router = DefaultRouter()
# LANG
router.register(r'v1/visual-test/classic/lang', LangEnpoints, basename='lang')
router.register(r'v1/visual-test/classic/lang/results', LangResultsEnpoints, basename='lang_results')

# ISHIHARA
router.register(r'v1/visual-test/classic/ishihara', IshiharaEndpoints, basename='ishihara')

urlpatterns = router.urls
