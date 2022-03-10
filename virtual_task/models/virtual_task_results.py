from djongo import models
import uuid

class VirtualTaskResultsModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name_virtual_task = models.CharField(max_length=300)
    code_virtual_task = models.CharField(max_length=50)
    total_hits = models.FloatField()
    total_errors = models.FloatField()
    group_test_ophthalmological = models.CharField(max_length=50)