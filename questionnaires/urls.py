
# Django rest framework
from rest_framework.routers import DefaultRouter

# Enpoints
from questionnaires.endpoints import QuestionnaireEndpoint

router = DefaultRouter()
# ophthalmological test
router.register(r'v1/tests/ophthalmological/virtual_task/questionaries', QuestionnaireEndpoint, basename='questionaries_virtual_test')


urlpatterns = router.urls
