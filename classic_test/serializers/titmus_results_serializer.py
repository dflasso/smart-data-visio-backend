# Django rest framework
from rest_framework import serializers

# Converters
from classic_test.converters import ConverterTitmusResultsRequest

class TitmusCirclesResultSerializer(serializers.Serializer):
    cirles_id = serializers.CharField(max_length=50)
    circle_name_spanish_correct = serializers.CharField(max_length=200)
    circle_name_english_correct = serializers.CharField(max_length=200)
    circle_name_spanish_selected = serializers.CharField(max_length=200)
    circle_name_english_selected = serializers.CharField(max_length=200)
    weighing_correct = serializers.FloatField()
    weighing_selected = serializers.FloatField()
    num_figure = serializers.IntegerField()
    is_correct = serializers.BooleanField()

    class Meta:
        abstract = True

class TitmusCirclesSummarySerializer(serializers.Serializer):
    id_test = serializers.CharField(max_length=20)
    observations = serializers.CharField(max_length=500,required = False)
    started_at = serializers.DateTimeField()
    finished_at = serializers.DateTimeField()

    results = TitmusCirclesResultSerializer(many=True)
    class Meta:
        abstract = True

class TitmusAnimalsResultSerializer(serializers.Serializer):
    animal_id = serializers.CharField(max_length=50)
    animal_name_spanish_correct = serializers.CharField(max_length=200)
    animal_name_english_correct = serializers.CharField(max_length=200)
    animal_name_spanish_selected = serializers.CharField(max_length=200)
    animal_name_english_selected = serializers.CharField(max_length=200)
    weighing_correct = serializers.FloatField()
    weighing_selected = serializers.FloatField()
    row = serializers.CharField(max_length=10)
    is_correct = serializers.BooleanField()

    class Meta:
        abstract = True

class TitmusAnimalsSummarySerializer(serializers.Serializer):
    id_test = serializers.CharField(max_length=100)
    observations = serializers.CharField(max_length=500, required = False)
    started_at = serializers.DateTimeField()
    finished_at = serializers.DateTimeField()
    results = TitmusAnimalsResultSerializer(many=True)

    class Meta:
        abstract = True

class TitmusHouseFlySerializer(serializers.Serializer):
    id_test = serializers.CharField(max_length=100)
    view_fly = serializers.BooleanField()
    observations = serializers.CharField(max_length=500, required = False)
    started_at = serializers.DateTimeField()
    finished_at = serializers.DateTimeField()

    class Meta:
        abstract = True


class TitmusResultsSerializer(serializers.Serializer):
    id = serializers.CharField( required = False)
    ticket_patient_tests = serializers.CharField(max_length=100)

    house_fly = TitmusHouseFlySerializer(required = False)
    animals_test = TitmusAnimalsSummarySerializer(required = False)
    circles_test = TitmusCirclesSummarySerializer(required = False)

class TitmusHouseFlyResultsSerializer(serializers.Serializer):
    id = serializers.CharField( required = False)
    ticket_patient_tests = serializers.CharField(max_length=100)

    house_fly = TitmusHouseFlySerializer()

    def create(self, validated_data):
        data =  ConverterTitmusResultsRequest.from_req_update_fly_results(**validated_data)
        return data

class TitmusAnimalsUpdateResultsSerializer(serializers.Serializer):
    id = serializers.CharField( required = False)
    ticket_patient_tests = serializers.CharField(max_length=100)

    animals_test = TitmusAnimalsSummarySerializer()

    def create(self, validated_data):
        data =  ConverterTitmusResultsRequest.from_req_update_animals_results(**validated_data)
        return data

class TitmusCirclesUpdateResultsSerializer(serializers.Serializer):
    id = serializers.CharField( required = False)
    ticket_patient_tests = serializers.CharField(max_length=100)

    circles_test = TitmusCirclesSummarySerializer()

    def create(self, validated_data):
        data =  ConverterTitmusResultsRequest.from_req_update_circles_results(**validated_data)
        return data