# Django
from django.urls import path, include

# Django rest framework
from rest_framework.routers import DefaultRouter

# Enpoints
from classic_test.endpoints import (IshiharaEndpoints,IshiharaResultsEndpoints, LangEnpoints, 
LangResultsEnpoints, TitmusAnimalsEndpoint, TitmusCirclesEndpoint, TitmusResultsEndpoints)

router = DefaultRouter()
# LANG
router.register(r'v1/visual-test/classic/lang', LangEnpoints, basename='lang')
router.register(r'v1/visual-test/classic/lang/results', LangResultsEnpoints, basename='lang_results')

# ISHIHARA
router.register(r'v1/visual-test/classic/ishihara', IshiharaEndpoints, basename='ishihara')
router.register(r'v1/visual-test/classic/ishihara/results', IshiharaResultsEndpoints, basename='ishihara_results')

# TITMUS
router.register(r'v1/visual-test/classic/titmus/animals', TitmusAnimalsEndpoint, basename='titmus-animals')
router.register(r'v1/visual-test/classic/titmus/cirlces', TitmusCirclesEndpoint, basename='titmus-circles')

router.register(r'v1/visual-test/classic/titmus/results', TitmusResultsEndpoints, basename='titmus-circles')

urlpatterns = router.urls
