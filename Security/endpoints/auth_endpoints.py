from rest_framework.views import APIView
from rest_framework.response import Response
from Security.serializers.auth_serializer  import LoginSerializer

class AuthEnpoints(APIView):
    
    def post(self, request, *args, **kwargs):
        """Handle authenticate users"""
        login_user_serializer = LoginSerializer(data=request.data)
        login_user_serializer.is_valid(raise_exception=True)
        user, jwt = login_user_serializer.save()
        
        return Response({ "jwt": jwt })
