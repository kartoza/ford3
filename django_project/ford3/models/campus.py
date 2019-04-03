from django.contrib.gis.db import models
from ford3.models.provider import Provider
from ford3.models.qualification import Qualification
from ford3.models.saqa_qualification import SAQAQualification


class Campus(models.Model):
    provider = models.ForeignKey(
        Provider,
        on_delete=models.CASCADE)
    name = models.CharField(
        blank=False,
        null=False,
        unique=False,
        help_text='',
        max_length=255)
    location = models.PointField(
      blank=True,
      null=True,
      help_text='The spatial point position of the campus')
    photo = models.FileField(
        blank=False,
        null=True,
        help_text='Representative photo of campus',
        upload_to='campus/photo'
    )
    telephone = models.CharField(
        blank=False,
        null=True,
        unique=False,
        help_text='',
        max_length=255)
    email = models.CharField(
        blank=False,
        null=True,
        unique=False,
        help_text='',
        max_length=255)
    max_students_per_year = models.IntegerField(
        blank=False,
        null=True,
        unique=False,
        help_text='')
    physical_address_street_name = models.CharField(
        blank=False,
        null=True,
        unique=False,
        help_text='',
        max_length=255)

    physical_address_city = models.CharField(
        blank=False,
        null=True,
        unique=False,
        help_text='',
        max_length=255)

    physical_address_postal_code = models.CharField(
        blank=False,
        null=True,
        unique=False,
        help_text='',
        max_length=255)

    postal_address_street_name = models.CharField(
        blank=False,
        null=True,
        unique=False,
        help_text='',
        max_length=255)

    postal_address_city = models.CharField(
        blank=False,
        null=True,
        unique=False,
        help_text='',
        max_length=255)

    postal_address_postal_code = models.CharField(
        blank=False,
        null=True,
        unique=False,
        help_text='',
        max_length=255)

    pass

    def save_form_data(self, form_data):
        for key, value in form_data.items():
            setattr(self, key, value)
        self.save()

    def save_qualifications(self, form_data):
        for saqa_id in form_data['saqa_ids'].split(' '):

            saqa_qualif = SAQAQualification.objects.get(saqa_id=saqa_id)

            qualif = Qualification(
                saqa_qualification=saqa_qualif,
                campus=self)
            qualif.save()

    def __str__(self):
        return f'{self.name} campus'
