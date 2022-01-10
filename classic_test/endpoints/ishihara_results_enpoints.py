# Django Rest Framework
from rest_framework import viewsets, status
from rest_framework.response import Response

# Serializaers
from classic_test.serializers.lang_ishihara_results_serializer import LangIshiharaResultSerializer

# Models
from classic_test.models.lang_ishihara_results_model import LangIshiharaResult


class IshiharaResultsEndpoints():
    
    def create(self, request, *args, **kwargs):
        """Registra los resultados de las prueba visual ishihara"""
        lang_results_serializer = LangIshiharaResultSerializer(data=request.data)
        lang_results_serializer.is_valid(raise_exception=True)

        return Response({"test" : "1"},  status = status.HTTP_201_CREATED)