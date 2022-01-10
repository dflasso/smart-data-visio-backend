from rest_framework import serializers

# Models
from classic_test.models.lang_ishihara_model import LangIshiharaTest

class ItemsCardSerializer(serializers.Serializer):
    item_id = serializers.CharField(max_length=50)
    description_english = serializers.CharField(max_length=200)
    description_spanish = serializers.CharField(max_length=200)
    weighing = serializers.FloatField(min_value=0.0)

    class Meta:
        abstract = True

class LangIshiharaSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=50, required = False)
    name_test_spanish = serializers.CharField(max_length=100)
    name_test_english = serializers.CharField(max_length=100)
    type_test = serializers.CharField(max_length=10,  required = False)

    items_card = ItemsCardSerializer(many=True)

    def create(self, validated_data):
        validated_data['type_test'] = self.context["type_test_default"]
        return LangIshiharaTest.objects.create(**validated_data)