# Django rest framework
from Security import models
from rest_framework import serializers

# Models
from Security.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'doc_identification', 'phone', 'profesion', 'birthday', 'id_profile']