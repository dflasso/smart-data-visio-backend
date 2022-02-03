# Django rest framwork
from rest_framework import serializers

# Model
from  questionnaires.models import QuestionnaireModel

class QuestionSerializer(serializers.Serializer):
    id_question = serializers.CharField(max_length=50)
    statement = serializers.CharField(max_length=100)
    answerLabel = serializers.CharField(max_length=100)
    answerValue = serializers.FloatField()
    answerMinValue = serializers.FloatField()
    answerMaxValue = serializers.FloatField()

    class Meta:
        managed = False



class QuestionnaireSerializer(serializers.Serializer):
    id = serializers.CharField(required = False)
    num_test_group = serializers.CharField(max_length=50)
    code_virtual_task = serializers.CharField(max_length=50)
    started_at = serializers.DateTimeField()
    finished_at = serializers.DateTimeField()
    observations = serializers.CharField(max_length=300, required = False, allow_blank= True )
    type = serializers.CharField(max_length=50)
    version = serializers.CharField(max_length=10)
    description = serializers.CharField(max_length=100)

    questions = QuestionSerializer(many=True)


    def create(self, validated_data):
        return QuestionnaireModel.objects.create(**validated_data)