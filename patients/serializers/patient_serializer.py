# Djano Rest Framework
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

# Models
from Security.models.user import User

class PatientSerializer(serializers.Serializer):
    id = serializers.CharField( required=False )

    email = serializers.CharField(
        max_length=100, 
        min_length=1,
        validators=[
            UniqueValidator(queryset=User.objects.all())
            ]
        )
    
    doc_identification = serializers.CharField(
        max_length=100, 
        min_length=1, required=False,
        validators=[
            UniqueValidator(queryset=User.objects.all())
            ] 
        )
    
    
    first_name = serializers.CharField(
        max_length=50, 
        min_length=2 )

    last_name = serializers.CharField(
        max_length=50, 
        min_length=2 )
    
    username = serializers.CharField(
        max_length=50, 
        min_length=9 )

    phone = serializers.CharField(
        max_length=20, 
        min_length=9,
        required=False )

    profesion = serializers.CharField(
        max_length=100,
        required=False )

    force = serializers.CharField(
        max_length=100,
        required=False )

    army = serializers.CharField(
        max_length=100,
        required=False )

    grade = serializers.CharField(
        max_length=100,
        required=False )
    
    birthday = serializers.CharField(required=False )