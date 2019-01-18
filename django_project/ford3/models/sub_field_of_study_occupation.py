from django.db import models


class SubFieldOfStudyOccupation(models.Model):
  sub_field_of_study_d = models.IntegerField(
    blank=False,
    null=False,
    unique=False,
    help_text='')
  occupation_id = models.IntegerField(
    blank=False,
    null=False,
    unique=False,
    help_text='')