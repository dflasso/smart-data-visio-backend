"""Modelo enfocao a registrar los datos de las pruebas ishihara y Lang"""
from djongo import models

class ItemsCard(models.Model):
    item_id = models.CharField(max_length=50, primary_key=True)
    description_english = models.CharField(max_length=100)
    description_spanish = models.CharField(max_length=100)
    weighing = models.FloatField()

    class Meta:
        managed = False

class LangIshiharaTest(models.Model):
    name_test_spanish = models.CharField(max_length=100)
    name_test_english = models.CharField(max_length=100)
    type_test = models.CharField(max_length=10)
    items_card = models.ArrayField(
        model_container= ItemsCard
    )

    objects = models.DjongoManager()
    
