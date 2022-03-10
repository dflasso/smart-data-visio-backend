from rest_framework import serializers

# model
from virtual_task.models import VirtualTaskResultsModel

class FileResultsUploadSerializer(serializers.Serializer):
    file = serializers.FileField()

class VirtualTaskResultsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VirtualTaskResultsModel
        fields = ['name_virtual_task', 'code_virtual_task', 'total_hits', 'total_errors', 'group_test_ophthalmological']


class VirtualTaskResultsDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VirtualTaskResultsModel
        fields = '__all__'