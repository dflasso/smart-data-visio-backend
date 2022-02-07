from djongo import models
import uuid

class QuestionModel(models.Model):
    id_question = models.CharField(max_length=50, primary_key=True)
    statement = models.CharField(max_length=300)
    answerLabel = models.CharField(max_length=100)
    answerValue = models.FloatField()
    answerMinValue = models.FloatField()
    answerMaxValue = models.FloatField()

    class Meta:
        managed = False


class QuestionnaireModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    num_test_group = models.CharField(max_length=50)
    code_virtual_task = models.CharField(max_length=50)
    started_at = models.DateTimeField()
    finished_at = models.DateTimeField()
    observations = models.CharField(max_length=300)
    type = models.CharField(max_length=50)
    version = models.CharField(max_length=10)
    description = models.CharField(max_length=100)

    questions = models.ArrayField(
        model_container=QuestionModel,
    )
