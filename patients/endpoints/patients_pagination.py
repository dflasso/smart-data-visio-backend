# Rest Framewrok Django
from email.policy import Policy
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status, viewsets
from rest_framework.viewsets import GenericViewSet
from rest_framework.pagination import PageNumberPagination

# Serializer
from patients.serializers import PatientSerializer, PatientUpdateSerializer
from Security.serializers import UserSerializer

# Models
from Security.models.user import User
from Security.models.profile import Profile

# DAOs
from Security.repositories import PatientsDao
from patients.repositories import MedicalHistoryDao


class PatientsPagination(GenericViewSet):

    def list(self, request):
        queryset = User.objects.all()
        page = self.paginate_queryset(queryset)
        serializer = UserSerializer(page, many=True)
        return self.get_paginated_response(serializer.data)