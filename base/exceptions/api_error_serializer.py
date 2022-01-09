from rest_framework import serializers

class SubErrorSerializer(serializers.Serializer):
    message_spanish = serializers.CharField(required = False)
    message_english = serializers.CharField()
    code = serializers.CharField(max_length=50, required = False)
    field_name_error = serializers.CharField(required = False)

    class Meta:
        abstract = True

class ApiErrorSerializer(serializers.Serializer):
    message_spanish = serializers.CharField(required = False)
    message_english = serializers.CharField()
    http_status = serializers.CharField(max_length=50)
    debug_message = serializers.CharField(required = False)

    sub_errors = SubErrorSerializer(many=True)
