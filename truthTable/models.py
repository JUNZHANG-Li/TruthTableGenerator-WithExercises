from django.db import models
from django.urls import reverse


# Create your models here.
class Generator(models.Model):
    formula = models.CharField(max_length=120)


class Exercise1(models.Model):
    question = models.CharField(max_length=120)
    formula0 = models.CharField(max_length=120)
    formula1 = models.CharField(max_length=120)
    formula2 = models.CharField(max_length=120)


class Exercise2(models.Model):
    question = models.CharField(max_length=120)
    values = models.CharField(max_length=120)
