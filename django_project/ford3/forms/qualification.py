from django import forms
from crispy_forms.helper import FormHelper
from ford3.enums.saqa_qualification_level import SaqaQualificationLevel
from ford3.models import (
    Interest,
    Occupation,
    Subject,
)


class QualificationForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(QualificationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.form_error_title = 'Form Errors'
        self.helper.help_text_inline = True


class QualificationDetailForm(QualificationForm):
    short_description = forms.CharField(
        label='Short Description of this Qualification:',
        help_text='*120 character max',
        required=False,
        widget=forms.Textarea(
            attrs={'rows': '5'}
        ),
        max_length=120
    )
    long_description = forms.CharField(
        label='Long Description of this Qualification:',
        help_text='*500 character max',
        required=False,
        widget=forms.Textarea,
        max_length=500
    )
    distance_learning = forms.TypedChoiceField(
        label='Distance Learning:',
        coerce=lambda x: x == 'True',
        required=False,
        choices=((True, 'Yes'), (False, 'No')),
        widget=forms.RadioSelect
    )


class QualificationDurationFeesForm(QualificationForm):
    full_time = forms.TypedChoiceField(
        label='Full-Time Qualification:',
        coerce=lambda x: x == 'True',
        required=False,
        choices=((True, 'Yes'), (False, 'No')),
        widget=forms.RadioSelect
    )

    part_time = forms.TypedChoiceField(
        label='Part-Time Qualification:',
        coerce=lambda x: x == 'True',
        required=False,
        choices=((True, 'Yes'), (False, 'No')),
        widget=forms.RadioSelect
    )

    duration = forms.IntegerField(
        label='Duration of the Qualification',
        required=False,
        widget=forms.NumberInput(
            attrs={'class': 'col-md-4'}
        )
    )

    duration_type = forms.ChoiceField(
        label=' ',
        choices=[
            ('month', 'Month'),
            ('year', 'Year')
        ],
        required=False,
        widget=forms.Select(
            attrs={'class': 'col-md-4'}
        )
    )

    total_cost = forms.DecimalField(
        label='Total Cost of Qualification',
        required=False,
        widget=forms.TextInput(
            attrs={'placeholder': 'ZAR'}
        )
    )

    total_cost_comment = forms.CharField(
        label='Cost Comment Field',
        help_text='*Any extra comments on '
                  'how Costs of this Qualification work',
        required=False,
        widget=forms.Textarea,
        max_length=255
    )


class QualificationRequirementsForm(QualificationForm):
    min_nqf_level = forms.ChoiceField(
        label='Required Entrance Qualification:',
        help_text='*List from SAQA',
        required=False,
        choices=[('', '-')] + [
            (level, level.value) for level in SaqaQualificationLevel]
    )

    interview = forms.TypedChoiceField(
        label='Is there an interview:',
        coerce=lambda x: x == 'True',
        required=False,
        choices=((True, 'Yes'), (False, 'No')),
        widget=forms.RadioSelect
    )

    portfolio = forms.TypedChoiceField(
        label='Require a portfolio:',
        coerce=lambda x: x == 'True',
        required=False,
        choices=((True, 'Yes'), (False, 'No')),
        widget=forms.RadioSelect
    )

    portfolio_comment = forms.CharField(
        label='What does the portfolio require:',
        required=False,
        widget=forms.Textarea(
            attrs={'rows': '5'}
        ),
        max_length=120
    )

    require_aps_score = forms.TypedChoiceField(
        label='Require an APS score:',
        coerce=lambda x: x == 'True',
        required=False,
        choices=((True, 'Yes'), (False, 'No')),
        widget=forms.RadioSelect
    )

    aps_calculator_link = forms.URLField(
        label='Link to APS Calculator on Website [if any]:',
        required=False,
        widget=forms.TextInput(
            attrs={'placeholder': 'www.example/aps.com'}
        )
    )

    require_certain_subjects = forms.TypedChoiceField(
        label='Does Qualification require certain subjects:',
        coerce=lambda x: x == 'True',
        required=False,
        choices=((True, 'Yes'), (False, 'No')),
        widget=forms.RadioSelect
    )

    subject = forms.ModelChoiceField(
        label='Subject 1:',
        queryset=Subject.objects.all(),
        required=False,
        widget=forms.Select(
            attrs={'class': 'col-md-4 subject-list'}
        )
    )

    subject_list = forms.CharField(
        required=False,
        widget=forms.HiddenInput(
            attrs={'id': 'subject-list'}
        )
    )

    minimum_score_list = forms.CharField(
        required=False,
        widget=forms.HiddenInput(
            attrs={'id': 'minimum-score-list'}
        )
    )


class QualificationInterestsAndJobsForm(QualificationForm):
    interest_list = forms.ModelMultipleChoiceField(
        label='Choose three interests associated to this Qualification:',
        queryset=Interest.objects.all(),
        required=False,
        widget=forms.SelectMultiple(
            attrs={
                'data-background-color': 'turquoise',
                'data-max-selected': '3'
            }
        )
    )

    occupation_list = forms.ModelMultipleChoiceField(
        label=(
            'Choose up to five Occupations that '
            'this Qualification could prepare you for:'
        ),
        queryset=Occupation.objects.all(),
        required=False,
        widget=forms.SelectMultiple(
            attrs={
                'data-background-color': 'gray',
                'data-max-selected': '5'
            }
        )
    )

    critical_skill = forms.TypedChoiceField(
        label=(
            'Does the qualification prepare for a '
            '<b>critical skills</b> occupation:'
        ),
        required=False,
        choices=((True, 'Yes'), (False, 'No')),
        widget=forms.RadioSelect
    )

    green_occupation = forms.TypedChoiceField(
        label=(
            'Does the qualification prepare for a <b>green</b> occupation:'
        ),
        required=False,
        choices=((True, 'Yes'), (False, 'No')),
        widget=forms.RadioSelect
    )

    high_demand_occupation = forms.TypedChoiceField(
        label=(
            'Does the qualification '
            'prepare for a <b>high demand</b> occupation:'
        ),
        required=False,
        choices=((True, 'Yes'), (False, 'No')),
        widget=forms.RadioSelect
    )


class QualificationImportantDatesForm(QualificationForm):
    date_start = forms.DateField(
        label='Application period start:',
        required=False,
        widget=forms.DateInput(
            attrs={'class': 'col-md-4'}
        )
    )

    date_end = forms.DateField(
        label='Application period end:',
        required=False,
        widget=forms.DateInput(
            attrs={'class': 'col-md-4'}
        )
    )

    other_event = forms.CharField(
        label='Other event [if any]:',
        required=False,
        widget=forms.TextInput(
            attrs={'placeholder': 'Title, eg, Exhibition'}
        )
    )

    event_date = forms.DateField(
        label='Event Date:',
        required=False,
        widget=forms.DateInput(
            attrs={'class': 'col-md-4'}
        )
    )
