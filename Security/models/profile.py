"""Modelo de enfocado a los perfiles que tendra cada usuario """
from djongo import models

class ResourcesProfile(models.Model):
    id_resource_parent = models.CharField(max_length=100, blank=True)
    id_resource = models.CharField(max_length=100)
    page_name = models.CharField(max_length=100)
    tab_name = models.CharField(max_length=100)
    url = models.CharField(max_length=100, blank=True)
    icon = models.CharField(max_length=100, blank=True)
    can_edit = models.BooleanField(default=False)
    can_create = models.BooleanField(default=False)
    can_read = models.BooleanField(default=True)

    class Meta:
        abstract = True



# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    resources = models.ArrayField(
        model_container= ResourcesProfile
    )


    