"""Modelo de enfocado a los perfiles que tendra cada usuario """
from djongo import models
from django import forms

class ResourcesProfile(models.Model):
    id_resource_parent = models.CharField(max_length=100)
    id_resource = models.UUIDField(unique=True)
    page_name = models.CharField(max_length=100)
    tab_name = models.CharField(max_length=100)
    url = models.URLField(blank=True)
    icon = models.CharField(max_length=100)
    can_edit = models.BooleanField(default=False)
    can_create = models.BooleanField(default=False)
    can_read = models.BooleanField(default=True)

    class Meta:
        abstract = True

class ResourcesProfileFrom(forms.ModelForm):
    class Meta: 
        model = ResourcesProfile
        fields = (
            'id_resource_parent', 'id_resource',
            'page_name',
            'tab_name',
            'url',
            'icon',
            'can_edit',
            'can_create',
            'can_read'
        )

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    resources = models.ArrayField(
        model_container=ResourcesProfile,
        model_form_class=ResourcesProfileFrom
    )

    objects = models.DjongoManager()

    