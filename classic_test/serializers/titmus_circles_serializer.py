from rest_framework import serializers

# Models
from classic_test.models import TitmusCircles

class TitmusCirclesSerializer(serializers.Serializer):
    cirles_id = serializers.CharField( required = False)
    circle_name_spanish = serializers.CharField(max_length=200)
    circle_name_english = serializers.CharField(max_length=200)
    weighing = serializers.FloatField()
    num_figure = serializers.IntegerField()
    is_correct = serializers.BooleanField()

    def create(self, validated_data):
        return TitmusCircles.objects.create(**validated_data)