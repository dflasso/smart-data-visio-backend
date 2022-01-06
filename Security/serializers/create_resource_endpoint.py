from rest_framework import serializers

class CreateResourceRequest(serializers.Serializer):
    page_name = serializers.CharField(
        max_length=100, 
        min_length=1, 
        allow_blank=False)
    
    tab_name = serializers.CharField(
        max_length=100, 
        min_length=1, 
        allow_blank=False)
    
    url = serializers.URLField(
        max_length=200, 
        min_length=1, 
        allow_blank=False )
    
    icon = serializers.CharField(
        max_length=100, 
        min_length=None, 
        allow_blank=True)

    
    id_resource_parent = serializers.CharField(
        max_length=100, 
        min_length=None, 
        allow_blank=True )