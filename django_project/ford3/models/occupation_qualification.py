from django.db import models


class OccupationQualification(models.Model):
  id = models.IntegerField(
    blank=False,
    null=False,
    unique=True,
    help_text='',
    primary_key=True)
  occupation_id = models.IntegerField(
    blank=False,
    null=False,
    unique=False,
    help_text='')
  qualitication_id = models.IntegerField(
    blank=False,
    null=False,
    unique=False,
    help_text='')