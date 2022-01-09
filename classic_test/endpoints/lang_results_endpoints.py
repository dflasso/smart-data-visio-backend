# Django Rest Framework
from rest_framework import viewsets, status
from rest_framework.response import Response

# Serializaers
from classic_test.serializers.lang_ishihara_results_serializer import LangIshiharaResultSerializer

# Models
from classic_test.models.lang_ishihara_results_model import LangIshiharaResult

# Constants
from classic_test.constants.type_classic_test import TypeClassicTest

# Converters
from classic_test.converters.lang_ishihara_results import lang_results_from_serializer_to_model

class LangResultsEnpoints(viewsets.ViewSet):
    
    def create(self, request, *args, **kwargs):
        """Registra los resultados de las prueba visual lang"""
        lang_results_serializer = LangIshiharaResultSerializer(data=request.data)
        lang_results_serializer.is_valid(raise_exception=True)
        lang_results_serializer.context["type_test_default"] = TypeClassicTest.LANG.value
        lang_results_model = lang_results_from_serializer_to_model(lang_results_serializer.save())
        LangIshiharaResult.objects.create(**lang_results_model)

        return Response(lang_results_model , status = status.HTTP_201_CREATED)