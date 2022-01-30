
# Django rest framework
from rest_framework.routers import DefaultRouter

# Enpoints
from legal_documents.endpoints import VirtualTestDocsEndpoints

router = DefaultRouter()
# ophthalmological test
router.register(r'v1/tests/ophthalmological/virtual-task/documents', VirtualTestDocsEndpoints, basename='legal_documents')


urlpatterns = router.urls
