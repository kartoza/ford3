from django.db import models


class Requirements(models.Model):
  id = models.IntegerField(
    primary_key=True,
    blank=False,
    null=False,
    unique=True,
    help_text='')
  description = models.CharField(
    blank=True,
    null=True,
    unique=False,
    help_text='',
    max_length=255)
  qualification_id = models.IntegerField(
    blank=False,
    null=False,
    unique=False,
    help_text='')
  assessment = models.BooleanField(
    blank=False,
    null=False,
    unique=False,
    help_text='')
  interview = models.BooleanField(
    blank=False,
    null=False,
    unique=False,
    help_text='')
  admission_point_score = models.IntegerField(
    blank=False,
    null=False,
    unique=False,
    help_text='')
  min_qualification = models.IntegerField(
    blank=False,
    null=False,
    unique=False,
    help_text='')

  def __str__(self):
    return self.description