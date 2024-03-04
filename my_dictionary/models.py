from django.db import models

# Create your models here.
class Dictionary(models.Model):
    original = models.CharField(max_length=100)
    translation = models.CharField(max_length=100)