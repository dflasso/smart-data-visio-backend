from rest_framework import serializers

# DAOs
from ophthalmological_test.repositories import OphthalmologicalTestDao

class OphthalmologicalTestSerializer(serializers.Serializer):
    id = serializers.CharField( required=False )
    patient_id = serializers.CharField(max_length=100)
    evaluator_id = serializers.CharField(max_length=100)
    created_at = serializers.DateTimeField(required=False )

    def create(self, validated_data):
        data = OphthalmologicalTestDao.create(**validated_data)
        return data