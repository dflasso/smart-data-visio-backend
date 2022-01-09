"""Modelo enfocao a registrar los datos de los resultados de ishihara y Lang"""
from djongo import models
from django.contrib.postgres.fields import ArrayField

class ItemsCardResult(models.Model):
    item_id = models.CharField(max_length=50, primary_key=True)
    correct_answer_spanish = models.CharField(max_length=100)
    correct_answer_english = models.CharField(max_length=100)
    value_correct_answer = models.FloatField()
    value_result_answer = models.FloatField()
    answer_correct = models.BooleanField()
    incorrect_answers = ArrayField(models.CharField(max_length=100, blank=True))

    class Meta:
        managed = False

class ResultsDetail(models.Model):
    id_test = models.CharField(max_length=20, primary_key=True)
    card_test_name_spanish = models.CharField(max_length=100, blank=True)
    card_test_name_english = models.CharField(max_length=100, blank=True)
    
    items_card = models.ArrayField(
        model_container= ItemsCardResult
    )

    class Meta:
        managed = False

class LangIshiharaResult(models.Model):
    id_ticket_patient_tests = models.CharField(max_length=20)
    type_test = models.CharField(max_length=10)
    observations = models.CharField(max_length=500, blank=True)
    started_at = models.DateTimeField()
    finished_at = models.DateTimeField()

    results = models.ArrayField(
        model_container= ResultsDetail
    )