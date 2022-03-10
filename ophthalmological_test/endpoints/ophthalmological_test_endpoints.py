# Django Rest Framework
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

# Serializer
from ophthalmological_test.serializers import OphthalmologicalTestSerializer
from Security.serializers import UserSerializer

# DAOs
from ophthalmological_test.repositories import OphthalmologicalTestDao
from Security.repositories import PatientsDao 

class OphthalmologicalTestEndpoints(viewsets.ViewSet):

    def list(self, request):
        list_patients = OphthalmologicalTestDao.find_all_by_patient_id_distinct()
        list_patients_parse = [int(id_patient) for id_patient in  list_patients]
        patients = PatientsDao.find_by_id_in_list(list_id_patients=list_patients_parse)
        patients_serializer = UserSerializer(patients, many = True)
        return Response(patients_serializer.data)

    def create(self, request):
        ophthalmological_test_serializer =  OphthalmologicalTestSerializer(data = request.data)
        ophthalmological_test_serializer.is_valid(raise_exception=True)
        ophthalmological_model = ophthalmological_test_serializer.save()
        ophthalmological_model_serializer =  OphthalmologicalTestSerializer(ophthalmological_model)
        return Response(ophthalmological_model_serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['get'])
    def find_groups_by_id_patient(self, request, pk=None):
        list_groups_test = OphthalmologicalTestDao.find_groups_test_by_patient_id(patient_id=pk)
        list_groups_test_serializer = OphthalmologicalTestSerializer(list_groups_test, many=True)
        return Response(list_groups_test_serializer.data)
