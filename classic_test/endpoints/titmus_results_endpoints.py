# Django Rest Framework
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

# Serializaers
from classic_test.serializers import (TitmusCirclesUpdateResultsSerializer, TitmusAnimalsUpdateResultsSerializer, 
TitmusHouseFlyResultsSerializer, TitmusResultsSerializer)

# Models
from classic_test.models import TitmusResults

class TitmusResultsEndpoints(viewsets.ViewSet):

    def retrieve(self, request, pk=None):
        return Response({"w": 0})
    
    @action(detail=False, methods=['put'])
    def add_house_fly_results(self, request):
        titmus_fly_results_serializer =  TitmusHouseFlyResultsSerializer(data=request.data)
        titmus_fly_results_serializer.is_valid(raise_exception=True)
        titmus_model = titmus_fly_results_serializer.save()
        titmus_model_serializer = TitmusResultsSerializer(titmus_model)
        return Response(titmus_model_serializer.data, status=status.HTTP_201_CREATED)

    
    @action(detail=False, methods=['put'])
    def add_animals_results(self, request):
        return Response({"w": 2})

    
    @action(detail=False, methods=['put'])
    def add_circles_results(self, request, pk=None):
        return Response({"w": 3})