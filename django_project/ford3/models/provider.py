from django.db import models


class Provider(models.Model):
    PROVIDER_TYPES = (
        'TVET College',
        'University',
        'Private Tertiary College',)

    name = models.CharField(
        blank=True,
        null=False,
        unique=False,
        help_text='',
        default='',
        max_length=255)
    provider_type = models.CharField(
        blank = False,
        null = False,
        unique = False,
        default='',
        help_text ='',
        max_length = 255)
    telephone = models.CharField(
        blank=False,
        null=True,
        unique=False,
        help_text='',
        max_length=12)
    website = models.CharField(
        blank=True,
        null=True,
        unique=False,
        help_text='',
        max_length=255)
    logo_url = models.CharField(
        blank=False,
        null=True,
        unique=False,
        help_text='',
        max_length=255)
    email = models.CharField(
        blank=False,
        null=False,
        unique=False,
        help_text='',
        max_length=255)
    admissions_contact_no = models.CharField(
        blank=False,
        null=True,
        unique=False,
        help_text='',
        max_length=255)
    postal_address = models.CharField(
        blank=False,
        null=True,
        unique=False,
        help_text='',
        max_length=4)
    physical_address_line_1 = models.CharField(
        blank = False,
        null = True,
        unique = False,
        help_text ='',
        max_length = 255)
    physical_address_line_2 = models.CharField(
        blank = False,
        null = True,
        unique = False,
        help_text ='',
        max_length = 255)
    physical_address_city = models.CharField(
        blank = False,
        null = True,
        unique = False,
        help_text ='',
        max_length = 255)

    pass

    def __str__(self):
        return self.name
