# Django Rest Framework
from questionnaires.models import questionnaire
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

# Serializer
from questionnaires.serializers import QuestionnaireSerializer

# DAOs
from questionnaires.repositories import QuestionnaireDAO

# Exceptions
from base.exceptions import BusinessRuleException


# Logger
from base.logger import log_error

# Contants
from base.constants import TypeAppError

# import module sys to get the type of exception
import sys

class QuestionnaireEndpoint(viewsets.ViewSet):

    @action(detail=True, methods=['get'])
    def find_by_params(self, request,  pk=None,  *args, **kwargs):
        """
        Find Questions and answers by:
        Path Variable
        pk -> num_test_group

        Query Params
        code_virtual_task 
        type
        version
        """
        code_virtual_task = ""
        type = ""
        version = ""

        try:
            query_params = request.query_params.dict()
            code_virtual_task = query_params['code_virtual_task']
            type = query_params['type']
            version = query_params['version']
        except: 
            details_error = {
                "type": sys.exc_info()[0],
                "value": sys.exc_info()[1],
                "treceback": sys.exc_info()[2]
            }
            log_error(action="QuestionnaireEndpoint.find_by_params",
                      message=f"Unexpedted Error in find Questionnaire",
                      details_error=details_error)
            raise BusinessRuleException(
                code=TypeAppError.PARAMS_REQUIRED_NULL,
                message_english="Required parameters are missing",
                message_spanish="Faltan los parámetros requeridos",
                status=status.HTTP_406_NOT_ACCEPTABLE
            )
        
        questionnaire = QuestionnaireDAO.find_by_num_test_group_and_code_virtual_task(
            num_test_group=pk,
            code_virtual_task=code_virtual_task,
            type=type,
            version=version
        )

        questionnaire_serializer =  QuestionnaireSerializer(questionnaire[0])

        
        return Response(questionnaire_serializer.data)


    
    def create(self, request):
        questionnarie_serializer = QuestionnaireSerializer(data = request.data)
        questionnarie_serializer.is_valid(raise_exception=True)
        questionnarie_serializer.save()
        return Response(questionnarie_serializer.data,  status=status.HTTP_201_CREATED )