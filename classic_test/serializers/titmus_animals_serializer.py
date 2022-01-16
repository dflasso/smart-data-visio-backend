from rest_framework import serializers

# Models
from classic_test.models import TitmusAnimals

class TitmusAnimalsSerializer(serializers.Serializer):
    animal_id = serializers.CharField( required = False)
    animal_name_spanish = serializers.CharField(max_length=200)
    animal_name_english = serializers.CharField(max_length=200)
    weighing = serializers.FloatField()
    row = serializers.CharField(max_length=10)
    order = serializers.IntegerField()
    is_correct = serializers.BooleanField()

    def create(self, validated_data):
        return TitmusAnimals.objects.create(**validated_data)