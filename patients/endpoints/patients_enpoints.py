# Rest Framewrok Django
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Serializer
from patients.serializers.patient_serializer import PatientSerializer
from Security.serializers import UserSerializer

# Models
from Security.models.user import User
from Security.models.profile import Profile

class PatientsApis(APIView):


    def get(self, request, *args, **kwargs): 
        """Obtiene todos los usuarios con el perfil: P01 (paciente) """
        profile_patients = Profile.objects.get(code='P01')

        if profile_patients is None:
            return Response({"code": "404-01"}, status = status.HTTP_404_NOT_FOUND)

        users = User.objects.all().filter(id_profile=str(profile_patients.id))

        patients_serializer = PatientSerializer(users, many=True)
        return Response(patients_serializer.data)
    
    def post(self, request, *args, **kwargs):
        """Registra un paciente.
        Se agrega un documento a la tabla User, 
        con el perfil por defecto de los pacientes (code =  P01)
        y con la contraseña por defecto: usertest12345
        """
        patient_serializer = PatientSerializer(data = request.data)
        patient_serializer.is_valid(raise_exception=True)
        patient_dict = patient_serializer.data

        profile_patients = Profile.objects.get(code='P01')

        if profile_patients is None:
            return Response({"code": "404-01"}, status = status.HTTP_404_NOT_FOUND)

        patient_dict['id_profile'] = str(profile_patients.id)
        patient_dict['password'] = 'usertest12345'

        user_data = User.objects.create(**patient_dict)
        user_data_serializer = UserSerializer(user_data)
        
        return Response(user_data_serializer.data, status = status.HTTP_201_CREATED)
        