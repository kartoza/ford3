from django.db import models


class SecondaryInstitutionTypeSubject(models.Model):
  subject_id = models.IntegerField(
    blank=False,
    null=False,
    unique=False,
    help_text='')
  secondary_institution_type_id = models.IntegerField(
    blank=False,
    null=False,
    unique=False,
    help_text='')