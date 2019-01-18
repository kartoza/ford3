from django.db import models
from ford3.models.qualification import Qualification


class Occupation(models.Model):
  qualification_id = models.ManyToManyField(Qualification)

  id = models.IntegerField(
    blank=False,
    null=False,
    unique=True,
    help_text='',
    primary_key=True)
  name = models.CharField(
    blank=False,
    null=False,
    unique=False,
    help_text='',
    max_length=255)
  description = models.CharField(
    blank=True,
    null=True,
    unique=False,
    help_text='',
    max_length=255)

  pass