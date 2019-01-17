from django.db import models


class Qualification(models.Model):
  id = models.IntegerField(
    primary_key=True,
    blank=False,
    null=False,
    unique=True,
    help_text='Key of qualification')
  subfield_of_study_id = models.IntegerField(
    blank=False,
    null=False,
    unique=False,
    help_text='')
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
  long_description = models.TextField(
    blank=False,
    null=False,
    unique=False,
    help_text='',)
  NQF_level = models.IntegerField(
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
  campus_id = models.IntegerField(
    blank=False,
    null=False,
    unique=False,
    help_text='')


  def __str__(self):
    return self.name