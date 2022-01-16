"""Modelo enfocao a registrar los datos de los resultados de Titmus"""
import uuid
from djongo import models

class TitmusCirclesResult(models.Model):
    cirles_id = models.CharField(max_length=50, primary_key=True)
    circle_name_spanish_correct = models.CharField(max_length=200)
    circle_name_english_correct = models.CharField(max_length=200)
    circle_name_spanish_selected = models.CharField(max_length=200)
    circle_name_english_selected = models.CharField(max_length=200)
    weighing_correct = models.FloatField()
    weighing_selected = models.FloatField()
    num_figure = models.IntegerField()
    is_correct = models.BooleanField()

    class Meta:
        managed = False

class TitmusCirclesSummary(models.Model):
    id_test = models.CharField(max_length=20, primary_key=True)
    observations = models.CharField(max_length=500, blank=True)
    started_at = models.DateTimeField()
    finished_at = models.DateTimeField()

    results = models.ArrayField(
         model_container=TitmusCirclesResult,
    )

    class Meta:
        managed = False

class TitmusAnimalsResult(models.Model):
    animal_id = models.CharField(max_length=50, primary_key=True)
    animal_name_spanish_correct = models.CharField(max_length=200)
    animal_name_english_correct = models.CharField(max_length=200)
    animal_name_spanish_selected = models.CharField(max_length=200)
    animal_name_english_selected = models.CharField(max_length=200)
    weighing_correct = models.FloatField()
    weighing_selected = models.FloatField()
    row = models.CharField(max_length=10)
    is_correct = models.BooleanField()

    class Meta:
        managed = False

class TitmusAnimalsSummary(models.Model):
    id_test = models.CharField(max_length=100, primary_key=True)
    observations = models.CharField(max_length=500, blank=True)
    started_at = models.DateTimeField()
    finished_at = models.DateTimeField()

    results = models.ArrayField(
         model_container=TitmusAnimalsResult,
    )

    class Meta:
        managed = False

class TitmusHouseFly(models.Model):
    id_test = models.CharField(max_length=100, primary_key=True)
    view_fly = models.BooleanField()
    observations = models.CharField(max_length=500, blank=True)
    started_at = models.DateTimeField()
    finished_at = models.DateTimeField()

    class Meta:
        managed = False


class TitmusResults(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ticket_patient_tests = models.CharField(max_length=20)

    house_fly = models.EmbeddedField(
        model_container=TitmusHouseFly
    )

    animals_test = models.EmbeddedField(
        model_container=TitmusAnimalsSummary
    )

    circles_test = models.EmbeddedField(
        model_container=TitmusCirclesSummary
    )
