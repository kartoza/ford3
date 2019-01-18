from django.db import models


class QualificationModule(models.Model):
  qualification = models.IntegerField(
    blank=False,
    null=False,
    unique=False,
    help_text='')
  module_id = models.IntegerField(
    blank=False,
    null=False,
    unique=False,
    help_text='')