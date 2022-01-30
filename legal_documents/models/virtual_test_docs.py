# Djongo 
from djongo import models 
from django.utils import timezone

def doc_directory_path(instance, filename):
    now = timezone.now()
    return f'pruebas_virtuales/{instance.name_virtual_test}/{instance.type_doc}/{now:%Y}/{now:%m}/{now:%d}/{filename}'

class VirtualTestDocs(models.Model):
    num_test = models.CharField(max_length=50)
    code_virtual_test = models.CharField(max_length=10)
    name_virtual_test = models.CharField(max_length=100)
    type_doc = models.CharField(max_length=100)
    code_type_doc = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    document = models.FileField(upload_to=doc_directory_path, blank=True, null=True)
