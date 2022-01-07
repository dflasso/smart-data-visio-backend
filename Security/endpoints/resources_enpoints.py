# Rest Framewrok Django
from rest_framework.decorators import api_view 
from rest_framework.response import Response

# Models
from Security.models.resources import Resources

#Serializers
from Security.serializers import ResourceSerializer

@api_view(['GET'])
def find_resources(request):
    resources = Resources.objects.all()
    resources_serializer = ResourceSerializer(resources, many=True)
    return Response(resources_serializer.data)

@api_view(['POST'])
def save_resource(request):
    resources_serializer = ResourceSerializer(data=request.data)
    resources_serializer.is_valid(raise_exception=True)
    resources_data = resources_serializer.data
    resources_saved = Resources.objects.create(**resources_data)
    resources_saved_serializer =  ResourceSerializer(resources_saved)
    return Response(resources_saved_serializer.data)