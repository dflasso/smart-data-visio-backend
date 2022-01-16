# Django Rest Framework
from rest_framework import viewsets, status
from rest_framework.response import Response

# Serializaers
from classic_test.serializers import TitmusAnimalsSerializer

# Model
from classic_test.models import TitmusAnimals

class TitmusAnimalsEndpoint(viewsets.ViewSet):
    
    def list(self, request, *args, **kwargs): 
        all_titmus_animals = TitmusAnimals.objects.all()
        all_titmus_animals = all_titmus_animals.order_by('order')
        all_titmus_animals = all_titmus_animals.order_by('row')

        all_titmus_animals_serializer = TitmusAnimalsSerializer(all_titmus_animals, many=True)

        return Response(all_titmus_animals_serializer.data)
    
    def create(self, request, *args, **kwargs):
        titmus_animal_serializer = TitmusAnimalsSerializer(data = request.data)
        titmus_animal_serializer.is_valid(raise_exception=True)

        new_titmus_animal = titmus_animal_serializer.save()
        
        new_titmus_animal_serializer = TitmusAnimalsSerializer(new_titmus_animal)
        
        return Response(new_titmus_animal_serializer.data , status = status.HTTP_201_CREATED )