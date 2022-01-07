"""Modelo enfocao a registrar los datos de las pruebas ishihara y Lang"""
from djongo import models

class ItemsCard(models.Model):
    description = models.CharField(max_length=100)
    weighing = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        abstract = True

class LangIshiharaTest(models.Model):
    name_test = models.CharField(max_length=100)
    type_test = models.CharField(max_length=10)
    items_card = models.ArrayField(
        model_container= ItemsCard
    )
    
