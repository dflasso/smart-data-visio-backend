# Django Rest Framework
from rest_framework import viewsets, status
from rest_framework.response import Response

# Serializaers
from classic_test.serializers import LangIshiharaResultSerializer, LangIshiharaResultDetailsSerializer

# Models
from classic_test.models.lang_ishihara_results_model import LangIshiharaResult

# Converters
from classic_test.converters.lang_ishihara_results import lang_results_from_serializer_to_model

# DAO
from classic_test.repositories.lang_ishihara_results_dao import LangIshiharaResultsDao

class LangResultsEnpoints(viewsets.ViewSet):
    
    def create(self, request, *args, **kwargs):
        """Registra los resultados de las prueba visual lang"""
        lang_results_serializer = LangIshiharaResultSerializer(data=request.data)
        lang_results_serializer.is_valid(raise_exception=True)
        lang_results_model = lang_results_from_serializer_to_model(lang_results_serializer.save())
        
        lang_results_model = LangIshiharaResultsDao.save_or_update_by_id_ticket_patient_tests(**lang_results_model)
        lang_results_model_serializer = LangIshiharaResultDetailsSerializer(lang_results_model)

        return Response(lang_results_model_serializer.data , status = status.HTTP_201_CREATED)