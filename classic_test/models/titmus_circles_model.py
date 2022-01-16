"""Modelo enfocao a registrar los datos de los circulos que se muestran en el test 
de TITMUS"""
from djongo import models
import uuid

class TitmusCircles(models.Model):
    cirles_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    circle_name_spanish = models.CharField(max_length=200)
    circle_name_english = models.CharField(max_length=200)
    weighing = models.FloatField()
    num_figure = models.IntegerField()
    is_correct = models.BooleanField()

    objects = models.DjongoManager()