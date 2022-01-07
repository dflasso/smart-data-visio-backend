"""Modelado de cada recurso o pagina que el usuario puede acceder"""
from djongo import models


class Resources(models.Model):
    page_name = models.CharField(max_length=100)
    tab_name = models.CharField(max_length=100)
    url = models.CharField(max_length=100, blank=True)
    icon = models.CharField(max_length=100)
    id_resource_parent = models.CharField(max_length=100, blank=True)


