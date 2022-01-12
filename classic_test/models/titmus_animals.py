"""Modelo enfocao a registrar los datos de los animales que se muestran en el test 
de TITMUS"""
import uuid
from djongo import models

class TitmusAnimals(models.Model):
    animal_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    animal_name_spanish = models.CharField(max_length=200)
    animal_name_english = models.CharField(max_length=200)
    weighing = models.FloatField()
    row = models.CharField(max_length=10)
    order = models.IntegerField()
    is_correct = models.BooleanField()

    objects = models.DjongoManager()