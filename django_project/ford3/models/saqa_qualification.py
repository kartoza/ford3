from django.db import models


class SAQAQualification(models.Model):
    # subjects = models.ManyToManyField(
    #     Subject,
    #     through='QualificationEntranceRequirementSubject')
    # campus = models.ForeignKey(
    #     Campus,
    #     on_delete=models.CASCADE)
    # sub_field_of_study = models.ForeignKey(
    #     SubFieldOfStudy,
    #     null=True,
    #     blank=True,
    #     on_delete=models.PROTECT)
    saqa_id = models.IntegerField(
        blank=False,
        null=False,
        help_text='')
    name = models.CharField(
        blank=False,
        null=False,
        help_text='',
        max_length=255)
    nqf_level = models.IntegerField(
        blank=True,
        null=True,
        help_text='')

    def __str__(self):
        return self.name
