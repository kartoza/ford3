from django.db import models

from ford3.models.qualification import import_qualifcations_from_scraped_file


class QualificationEvent(models.Model):
    qualification = models.ForeignKey(
        import_qualifcations_from_scraped_file,
        on_delete=models.CASCADE)
    name = models.CharField(
        blank=True,
        null=True,
        help_text='',
        max_length=255)
    date_start = models.DateField(
        blank=True,
        null=True,
        help_text='')
    date_end = models.DateField(
        blank=True,
        null=True,
        help_text='')
    event_date = models.DateField(
        blank=True,
        null=True
    )
    other_event = models.CharField(
        blank=True,
        null=True,
        max_length=255
    )
    http_link = models.CharField(
        blank=True,
        null=True,
        help_text='',
        max_length=255)

    def __unicode__(self):
        return self.name
