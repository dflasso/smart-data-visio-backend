# Rest Framewrok Django
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Serializer
from Security.serializers import ProfileSerializer

# Models
from Security.models.profile import Profile

class ProfileApis(APIView):

    
    def get(self, request, *args, **kwargs): 
       profiles = Profile.objects.all()
       profiles_serializer = ProfileSerializer(profiles, many=True)
       return Response(profiles_serializer.data)


    
    def post(self, request, *args, **kwargs):
        profile_serializer = ProfileSerializer(data = request.data)
        profile_serializer.is_valid(raise_exception=True)
        profile_serializer.save()
        return Response(profile_serializer.data, status = status.HTTP_201_CREATED)