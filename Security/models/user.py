from djongo import models
from django import forms

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(
        unique=True,
        error_messages={
            "unique": "email already used"
        }
    )

    doc_identification = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    
    profesion = models.CharField(max_length=100)
    force = models.CharField(max_length=100)
    army = models.CharField(max_length=100)
    grade = models.CharField(max_length=100)

    birthday = models.DateField()    

    id_profile = models.CharField(max_length=100, blank=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [ "username", "first_name" , "last_name" ]

    