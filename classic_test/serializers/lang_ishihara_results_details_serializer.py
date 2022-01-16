from rest_framework import serializers

class ItemsCardResultSerializer(serializers.Serializer):
    item_id = serializers.CharField(max_length=50)
    correct_answer_spanish = serializers.CharField(max_length=100, required = False)
    correct_answer_english = serializers.CharField(max_length=100, required = False)
    value_result_answer = serializers.FloatField( required = False)
    answer_correct = serializers.FloatField( required = False)
    answer_correct = serializers.BooleanField()
    incorrect_answers = serializers.ListField(child=serializers.CharField(), required = False)

    class Meta:
        abstract = True

class ResultsDetailSerializer(serializers.Serializer):
    id_test = serializers.IntegerField(min_value=0)
    card_test_name_spanish = serializers.CharField(max_length=100, required = False)
    card_test_name_english = serializers.CharField(max_length=100, required = False)
    observations = serializers.CharField(max_length=500,  required = False)
    started_at = serializers.DateTimeField()
    finished_at = serializers.DateTimeField()
    
    items_card = ItemsCardResultSerializer(many=True)

    class Meta:
        abstract = True

class LangIshiharaResultDetailsSerializer(serializers.Serializer):
    id = serializers.CharField( required = False)
    ticket_patient_tests = serializers.CharField(max_length=100)
    type_test = serializers.CharField(max_length=10,  required = False)
    results = ResultsDetailSerializer(many=True)

    def create(self, validated_data):
        return {**validated_data}