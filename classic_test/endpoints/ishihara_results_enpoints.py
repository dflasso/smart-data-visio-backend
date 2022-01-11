# Django Rest Framework
from rest_framework import viewsets, status
from rest_framework.response import Response

# Serializaers
from classic_test.serializers import LangIshiharaResultSerializer, LangIshiharaResultDetailsSerializer

# Converter
from classic_test.converters import ishihara_results_from_serializer_to_model

# DAO
from classic_test.repositories.lang_ishihara_results_dao import LangIshiharaResultsDao


class IshiharaResultsEndpoints(viewsets.ViewSet):
    
    def create(self, request, *args, **kwargs):
        """Registra los resultados de las prueba visual ishihara"""
        ishihara_results_serializer = LangIshiharaResultSerializer(data=request.data)
        ishihara_results_serializer.is_valid(raise_exception=True)

        ishihara_results_model = ishihara_results_from_serializer_to_model(ishihara_results_serializer.save())
        
        ishihara_results_model = LangIshiharaResultsDao.save_or_update_by_id_ticket_patient_tests(**ishihara_results_model)
        ishihara_results_model_serializer = LangIshiharaResultDetailsSerializer(ishihara_results_model)

        return Response(ishihara_results_model_serializer.data,  status = status.HTTP_201_CREATED)