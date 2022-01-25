# Djano Rest Framework
from rest_framework import serializers
# Model
from patients.models import MedicalHistory
# DAOs
from patients.repositories import MedicalHistoryDao

class DiseasesSerializer(serializers.Serializer):
    id_diseases = serializers.CharField(max_length=50)
    name = serializers.CharField(max_length=100)
    indications = serializers.CharField(max_length=300, allow_blank=True )
    observations = serializers.CharField(max_length=300, allow_blank=True )

    class Meta:
        abstract = True


class EyeglassesPatientSerializer(serializers.Serializer):
    id_eyeglasses = serializers.CharField(max_length=50)
    use = serializers.BooleanField(default=False)
    measurement = serializers.FloatField()
    started_use_at = serializers.DateTimeField()

    class Meta:
        abstract = True


class MedicalHistorySerializer(serializers.Serializer):
    patient_id = serializers.CharField(max_length=50)
    eyeglasses = EyeglassesPatientSerializer(  )
    diseases = DiseasesSerializer(many=True, )

    def create(self, validated_data):
        medical_history_model = MedicalHistoryDao.create_or_update(**validated_data)
        return medical_history_model
