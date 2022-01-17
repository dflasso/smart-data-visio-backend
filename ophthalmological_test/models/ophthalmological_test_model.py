# Djongo 
from djongo import models 

class OphthalmologicalTest(models.Model):
    patient_id = models.CharField(max_length=100)
    evaluator_id = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = models.DjongoManager()