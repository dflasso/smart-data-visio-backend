from rest_framework import serializers
from rest_framework.validators import UniqueValidator
# Models
from Security.models.profile import  Profile

class ResourcesProfileSerializer(serializers.Serializer):
    id_resource_parent = serializers.CharField(max_length=100,
        required=False)
    id_resource = serializers.CharField()
    page_name = serializers.CharField(max_length=100)
    tab_name = serializers.CharField(max_length=100)
    url = serializers.CharField(required=False)
    icon = serializers.CharField(max_length=100,
        required=False)
    can_edit = serializers.BooleanField(default=False)
    can_create = serializers.BooleanField(default=False)
    can_read = serializers.BooleanField(default=True)

class ProfileSerializer(serializers.Serializer):
    id = serializers.CharField( required=False )

    name = serializers.CharField(
        max_length=100, 
        min_length=3,
        required=False )
    
    code = serializers.CharField(
        max_length=100, 
        min_length=3,
        validators=[
            UniqueValidator(queryset=Profile.objects.all())
            ]
        )
    
    resources = ResourcesProfileSerializer(many=True)

    def create(self, data):
        profile = Profile.objects.create(**data)
        return profile