from rest_framework import serializers

class ResourceSerializer(serializers.Serializer):
    id = serializers.CharField( required=False )

    page_name = serializers.CharField(
        max_length=100, 
        min_length=1)
    
    tab_name = serializers.CharField(
        max_length=100, 
        min_length=1)
    
    url = serializers.CharField(
        max_length=200, 
        min_length=1,
        required=False )
    
    icon = serializers.CharField(
        max_length=100, 
        min_length=None)

    
    id_resource_parent = serializers.CharField(
        max_length=100, 
        min_length=None, 
        required=False )
