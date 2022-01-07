"""
Serializer that check credentials, JWT 
"""

# Django
from django.contrib.auth import authenticate

# Django Rest Framework
from rest_framework import serializers

# Providers
from Security.providers import jwt_provider_from_user

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(trim_whitespace=False, min_length=8)

    def validate(self, data):
        """Check crendentials
        @see https://docs.djangoproject.com/en/4.0/topics/auth/default/
        """
        user = authenticate(username=data['email'], password=data['password'])
        if not user:
            # No backend authenticated the credentials
            raise serializers.ValidationError("Invalid Credentials")
        
        self.context['user'] = user

        return data
    
    def create(self, data):
        user  = self.context['user']
        jwt = jwt_provider_from_user(user=user, time_life_jwt=30)
        return user, jwt
