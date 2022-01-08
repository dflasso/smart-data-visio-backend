from rest_framework import serializers

class ItemsCardSerializer(serializers.Serializer):
    description = serializers.CharField(max_length=200)
    weighing = serializers.CharField(max_length=200)

    class Meta:
        abstract = True

class LangIshiharaSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=200, required = False)
    name_test = serializers.CharField(max_length=200)
    type_test = serializers.CharField(max_length=200)

    items_card = ItemsCardSerializer(many=True)