# Django rest framwork
from rest_framework.serializers import ModelSerializer

# Models 
from legal_documents.models import VirtualTestDocs

class VirtualTestDocsSerializerCreate(ModelSerializer):
    class Meta:
        model = VirtualTestDocs
        fields = ["num_test", "code_virtual_test", "name_virtual_test", "type_doc", "code_type_doc", "document"]

class VirtualTestDocsSerializerReadOnly(ModelSerializer):
    class Meta:
        model = VirtualTestDocs
        fields = ["id", "num_test", "code_virtual_test", "name_virtual_test", "type_doc", "code_type_doc", "document"]


class VirtualTestDocsSerializerUpdate(ModelSerializer):
    class Meta:
        model = VirtualTestDocs
        fields = ["id", "document"]

    def save(self, *args, **kwargs):
        if self.instance.avatar:
            self.instance.avatar.delete()
        return super().save(*args, **kwargs)
