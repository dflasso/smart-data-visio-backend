# Django Rest Framework
from rest_framework import viewsets, status
from rest_framework.response import Response

# Serializaers
from classic_test.serializers import TitmusCirclesSerializer

# Model
from classic_test.models import TitmusCircles

class TitmusCirclesEndpoint(viewsets.ViewSet):
    
    def list(self, request, *args, **kwargs): 
        all_titmus_circles = TitmusCircles.objects.all()
        all_titmus_circles = all_titmus_circles.order_by('num_figure')

        all_titmus_circles_serializer = TitmusCirclesSerializer(all_titmus_circles, many=True)

        return Response(all_titmus_circles_serializer.data)
    
    def create(self, request, *args, **kwargs):
        titmus_circle_serializer = TitmusCirclesSerializer(data = request.data)
        titmus_circle_serializer.is_valid(raise_exception=True)

        new_titmus_circle = titmus_circle_serializer.save()
        
        new_titmus_circle_serializer = TitmusCirclesSerializer(new_titmus_circle)
        
        return Response(new_titmus_circle_serializer.data , status = status.HTTP_201_CREATED )