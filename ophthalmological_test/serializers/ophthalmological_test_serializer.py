from rest_framework import serializers

class OphthalmologicalTestSerializer(serializers.Serializer):
    id = serializers.CharField( required=False )
    patient_id = serializers.CharField(max_length=100)
    evaluator_id = serializers.CharField(max_length=100)
    created_at = serializers.DateTimeField(required=False )