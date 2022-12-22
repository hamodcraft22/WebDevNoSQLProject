# django_project/users/models.py
from django.contrib.auth.models import AbstractUser
from djongo import models

class CustomUser(AbstractUser):
    address = models.CharField(max_length=150, blank=True)
    country = models.CharField(max_length=50, blank=True)
    birthDate = models.DateField(null=True)

    def __str__(self):
        return self.username
