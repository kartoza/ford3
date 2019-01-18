from django.db import models


class Campus(models.Model):
  id = models.IntegerField(
    blank=False,
    null=False,
    unique=True,
    help_text='',
    primary_key=True)
  provider_id = models.IntegerField(
    blank=False,
    null=False,
    unique=False,
    help_text='')
  name = models.CharField(
    blank=False,
    null=False,
    unique=False,
    help_text='',
    max_length=255)