# Rest Framewrok Django
from rest_framework.decorators import api_view 
from rest_framework.response import Response

# Models
from Security.models.resources import Resources

#Serializers
from Security.serializers import CreateResourceRequest

@api_view(['GET'])
def find_resources(request):
    resources = Resources.objects.all()
    resources_serializer = CreateResourceRequest(resources, many=True)
    return Response(resources_serializer.data)