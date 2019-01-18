from django.db import models
from ford3.models.subject import Subject
from ford3.models.campus import Campus
from ford3.models.sub_field_of_study import SubFieldOfStudy
from ford3.models.module import Module


class Qualification(models.Model):
  subjects = models.ManyToManyField(
    Subject,
    through='QualificationEntranceRequirementsSubjects')
  campus_id = models.ForeignKey(Campus)
  sub_field_of_study_id = models.ForeignKey(SubFieldOfStudy)
  modules = models.ManyToManyField(Module)

  id = models.IntegerField(
    blank=False,
    null=False,
    unique=True,
    help_text='Key of qualification',
    primary_key=True)
  qualification_id = models.IntegerField(
    blank=False,
    null=False,
    unique=False,
    help_text='')
  saqa_id = models.IntegerField(
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
  short_description = models.CharField(
    blank=False,
    null=False,
    unique=False,
    help_text='',
    max_length=255)
  long_description = models.CharField(
    blank=False,
    null=False,
    unique=False,
    help_text='',
    max_length=255)
  nqf_level = models.IntegerField(
    blank=False,
    null=False,
    unique=False,
    help_text='')
  duration_in_months = models.IntegerField(
    blank=False,
    null=False,
    unique=False,
    help_text='')
  full_time = models.BooleanField(
    blank=False,
    null=False,
    unique=False,
    help_text='')
  part_time = models.BooleanField(
    blank=False,
    null=False,
    unique=False,
    help_text='')
  credits_after_completion = models.IntegerField(
    blank=False,
    null=False,
    unique=False,
    help_text='')
  distance_learning = models.BooleanField(
    blank=False,
    null=False,
    unique=False,
    help_text='')
  estimated_annual_fee = models.IntegerField(
    blank=False,
    null=False,
    unique=False,
    help_text='')

