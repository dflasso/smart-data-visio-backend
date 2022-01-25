# Rest Framewrok Django
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status, viewsets

# Serializer
from patients.serializers import PatientSerializer, MedicalHistorySerializer
from Security.serializers import UserSerializer

# Models
from Security.models.user import User
from Security.models.profile import Profile

# DAOs
from Security.repositories import PatientsDao
from patients.repositories import MedicalHistoryDao

class MedicalHistoryApis(viewsets.ViewSet):
    
    @action(detail=True, methods=['get'])
    def find_by_patient_id(self, request,  pk=""):
        medical_history = MedicalHistoryDao.find_by_id_patient(patient_id=pk)
        medical_history_serializer = MedicalHistorySerializer(medical_history)
        return Response(medical_history_serializer.data)

    def create(self, request):
        medical_history_serializer = MedicalHistorySerializer(data = request.data)
        medical_history_serializer.is_valid(raise_exception=True)
        medical_history_serializer.save()
        return Response(medical_history_serializer.data, status = status.HTTP_201_CREATED)
        