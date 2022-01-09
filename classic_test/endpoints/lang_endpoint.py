# Django Rest Framework
from rest_framework import viewsets, status
from rest_framework.response import Response

# Serializaers
from classic_test.serializers import LangIshiharaSerializer

# Models
from classic_test.models.lang_ishihara_model import LangIshiharaTest

# Constants
from classic_test.constants.type_classic_test import TypeClassicTest

class LangEnpoints(viewsets.ViewSet):
    
    def list(self, request, *args, **kwargs): 
        all_test =  LangIshiharaTest.objects.all()
        lang_test = all_test.filter(type_test=TypeClassicTest.LANG.value)
        
        lang_test_serializer = LangIshiharaSerializer(lang_test, many=True)

        return Response(lang_test_serializer.data)

    def create(self, request, *args, **kwargs):
        """
        Create new card of the Test Lang
        """
        lang_test_serializer = LangIshiharaSerializer(data = request.data)
        lang_test_serializer.is_valid(raise_exception=True)
        lang_test_serializer.context["type_test_default"] = TypeClassicTest.LANG.value

        lang_test_saved  =  lang_test_serializer.save()
        lang_test_saved_serializer = LangIshiharaSerializer(lang_test_saved)
        
        return Response(lang_test_saved_serializer.data, status = status.HTTP_201_CREATED)
