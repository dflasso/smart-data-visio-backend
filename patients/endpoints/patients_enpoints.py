# Rest Framewrok Django
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status, viewsets
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

class PatientsApis(viewsets.ViewSet):

    def list(self, request):
        """Obtiene todos los usuarios con el perfil: P01 (paciente) """
        profile_patients = Profile.objects.get(code='P01')

        if profile_patients is None:
            return Response({"code": "404-01"}, status=status.HTTP_404_NOT_FOUND)

        users = User.objects.all().filter(id_profile=str(profile_patients.id))

        patients_serializer = UserSerializer(users, many=True)
        return Response(patients_serializer.data)

    def create(self, request):
        """Registra un paciente.
        Se agrega un documento a la tabla User, 
        con el perfil por defecto de los pacientes (code =  P01)
        y con la contraseña por defecto: usertest12345
        """
        patient_serializer = PatientSerializer(data=request.data)
        patient_serializer.is_valid(raise_exception=True)
        patient_dict = patient_serializer.data

        profile_patients = Profile.objects.get(code='P01')

        if profile_patients is None:
            return Response({"code": "404-01"}, status=status.HTTP_404_NOT_FOUND)

        patient_dict['id_profile'] = str(profile_patients.id)
        patient_dict['password'] = 'usertest12345'
        eyeglasses = patient_dict['eyeglasses']
        diseases = patient_dict['diseases']

        user_data_dict = patient_dict
        del user_data_dict['eyeglasses']
        del user_data_dict['diseases']
        user_data = User.objects.create(**user_data_dict)
        user_data_serializer = UserSerializer(user_data)

        MedicalHistoryDao.create_after_save_patient(eyeglasses=eyeglasses,
                                                    diseases=diseases,
                                                    id_patient=str(user_data.id))

        return Response(user_data_serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['get'])
    def find_by_num_document(self, request,  pk=""):
        patient = PatientsDao.find_by_num_document(num_document=pk)
        patient_serializer = UserSerializer(patient)
        return Response(patient_serializer.data)

    @action(detail=True, methods=['get'])
    def find_by_match_by_param(self, request,  pk=""):
        query_params = request.query_params.dict()
        patients = PatientsDao.find_match_in_many_fields(field=pk, limit=int(query_params['limit']), offset=int(query_params['offset']) )
        patient_serializer = UserSerializer(patients, many=True)
        return Response(patient_serializer.data)

    def update(self, request, pk=None):
        patient_serializer = PatientUpdateSerializer(data=request.data)
        patient_serializer.is_valid(raise_exception=True)
        
        """Get data"""
        patient_dict = patient_serializer.data
        eyeglasses = patient_dict['eyeglasses']
        diseases = patient_dict['diseases']

        """Remove extra data"""
        del patient_dict['eyeglasses']
        del patient_dict['diseases']

        """Update Patient"""
        patient_saved = PatientsDao.update({
                            "id": pk,
                            **patient_dict
                        })
                        
        """Update medical history"""
        MedicalHistoryDao.create_after_save_patient(eyeglasses=eyeglasses,
                                                    diseases=diseases,
                                                    id_patient=str(pk))

        return Response(patient_serializer.data, status=status.HTTP_201_CREATED)
