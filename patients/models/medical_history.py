from djongo import models


class Diseases(models.Model):
    id_diseases = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=100)
    indications = models.CharField(max_length=300, blank=True)
    observations = models.CharField(max_length=300, blank=True)

    class Meta:
        managed = False


class EyeglassesPatient(models.Model):
    id_eyeglasses = models.CharField(max_length=50, primary_key=True)
    use = models.BooleanField()
    measurement = models.FloatField()
    started_use_at = models.DateTimeField()

    class Meta:
        managed = False


class MedicalHistory(models.Model):
    patient_id = models.CharField(max_length=50,
                                  unique=True,
                                  error_messages={
                                      "unique": "patient_id already used"
                                  })

    eyeglasses = models.EmbeddedField(
        model_container=EyeglassesPatient
    )

    diseases = models.ArrayField(
        model_container=Diseases,
    )
