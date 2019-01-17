from django.db import models


class QualificationEntranceRequirementSubjects(models.Model):
  id = models.IntegerField(
    primary_key=True,
    blank=False,
    null=False,
    unique=True,
    help_text='')
  qualification_id = models.CharField(
    blank=False,
    null=False,
    unique=False,
    help_text='',
    max_length=255)
  subject_id = models.CharField(
    blank=False,
    null=False,
    unique=False,
    help_text='',
    max_length=255)
  minimum_score = models.IntegerField(
    blank=False,
    null=False,
    unique=False,
    help_text='')
  required = models.BooleanField(
    blank=False,
    null=False,
    unique=False,
    help_text='')