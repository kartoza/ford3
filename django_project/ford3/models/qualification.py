from django.db import models
from ford3.models.saqa_qualification import SAQAQualification
from ford3.models.requirement import Requirement


class Qualification(models.Model):
    subjects = models.ManyToManyField(
        'ford3.subject',
        through='QualificationEntranceRequirementSubject')
    campus = models.ForeignKey(
        'ford3.campus',
        on_delete=models.CASCADE)
    saqa_qualification = models.ForeignKey(
        SAQAQualification,
        null=True,
        on_delete=models.PROTECT)
    occupations = models.ManyToManyField(
        'ford3.occupation',
        blank=True)
    interests = models.ManyToManyField(
        'ford3.interest',
        blank=True)
    name = models.CharField(
        blank=False,
        null=False,
        unique=False,
        help_text="The qualification's name",
        max_length=255)
    short_description = models.CharField(
        blank=True,
        null=True,
        help_text="A short description of what the qualification entails",
        max_length=120)
    long_description = models.CharField(
        blank=True,
        null=True,
        help_text="A longer description of the qualification for the student"
                  " who is interested and would like to know more",
        max_length=500)
    duration_in_months = models.IntegerField(
        blank=True,
        null=True,
        help_text="How long the qualification takes to complete (in months)")
    full_time = models.BooleanField(
        blank=True,
        null=True,
        default=False,
        help_text="Can this qualification be completed on a full-time basis?")
    part_time = models.BooleanField(
        blank=True,
        null=True,
        default=False,
        help_text="Can this qualification be completed on a part-time basis?")
    credits_after_completion = models.IntegerField(
        blank=True,
        null=True,
        help_text="How many credits are awarded after completion?")
    distance_learning = models.BooleanField(
        blank=True,
        null=True,
        default=False,
        help_text="Does this qualification have a distance learning option?")
    completion_rate = models.IntegerField(
        blank=True,
        null=True,
        help_text="What has the completion rate for this qualifcation been?",
        default=0)
    total_cost = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        blank=True,
        null=True,
        help_text="What is the total cost to complete this qualification?")
    total_cost_comment = models.CharField(
        blank=True,
        null=True,
        help_text="Any comments regarding the cost and payment options of "
                  "this qualification should be filled in here",
        max_length=255)
    critical_skill = models.BooleanField(
        blank=True,
        null=True,
        help_text="Would the skill obtained by completing this qualification "
                  "be considered a critical skill?",
        default=False)
    green_occupation = models.BooleanField(
        blank=True,
        null=True,
        help_text="Would the occupations this qualification prepares you for "
                  "be considered environmentally friendly?",
        default=False)
    high_demand_occupation = models.BooleanField(
        blank=True,
        null=True,
        help_text="Are the occupations this qualification prepares you for "
                  "in high demand?",
        default=False)

    def __str__(self):
        return self.saqa_qualification.name

    @property
    def requirements(self):

        requirement_query = Requirement.objects.filter(
            qualification__id=self.id).order_by('id').values()
        return list(requirement_query)

    def add_events(self, qualification_events):
        if len(qualification_events) == 0:
            return
        for each_qualification_event in qualification_events:
            each_qualification_event.qualification = self
            each_qualification_event.save()
