import datetime
from django.urls import reverse
from django.test import TestCase
from django.test.utils import override_settings
from ford3.tests.models.model_factories import ModelFactories
from ford3.models.qualification import Qualification
from ford3.models.qualification_entrance_requirement_subject import (
    QualificationEntranceRequirementSubject
)
from ford3.models.qualification_event import QualificationEvent
from ford3.models.requirement import Requirement
from ford3.views.qualification_wizard import QualificationFormWizardDataProcess


@override_settings(
    STATICFILES_STORAGE='pipeline.storage.NonPackagingPipelineStorage',
    PIPELINE_ENABLED=False)
class TestQualificationWizard(TestCase):
    wizard_step_1_data = {
        'session_contact_wizard-current_step': '0',
    }
    wizard_form_data = {
        'short_description': 'short_description',
        'long_description': 'long_description',
        'distance_learning': '',
        'full_time': '',
        'part_time': '',
        'duration': 1,
        'duration_type': 'month',
        'total_cost': None,
        'total_cost_comment': '',
        'min_nqf_level': '',
        'interview': '',
        'portfolio': '',
        'portfolio_comment': '',
        'require_aps_score': '',
        'aps_calculator_link': '',
        'require_certain_subjects': '',
        'subject': None,
        'interest_list': [],
        'occupation_list': [],
        'critical_skill': '',
        'green_occupation': '',
        'high_demand_occupation': '',
        'date_start': None,
        'date_end': None,
        'other_event': '',
        'event_date': None,
        'subject_list': '1,2',
        'minimum_score_list': '-1,2'
    }

    def setUp(self):
        self.qualification = ModelFactories.get_qualification_test_object(
            new_id=1
        )

        self.wizard_url = reverse(
            'edit-qualification',
            args=(
                self.qualification.campus.provider.id,
                self.qualification.campus.id,
                self.qualification.id))

        self.subject_1 = ModelFactories.get_subject_test_object(
            new_id=1
        )
        self.subject_2 = ModelFactories.get_subject_test_object(
            new_id=2
        )
        self.qualification_data_process = QualificationFormWizardDataProcess(
            qualification=self.qualification
        )

    def test_validate_data(self):
        self.assertTrue(True)

    def test_initial_call(self):
        response = self.client.get(self.wizard_url)
        wizard = response.context['wizard']
        self.assertEqual(response.status_code, 200)
        self.assertEqual(wizard['steps'].current, '0')
        self.assertEqual(wizard['steps'].step0, 0)
        self.assertEqual(wizard['steps'].step1, 1)
        self.assertEqual(wizard['steps'].last, '4')
        self.assertEqual(wizard['steps'].prev, None)
        self.assertEqual(wizard['steps'].next, '1')
        self.assertEqual(wizard['steps'].count, 5)

    def test_duration_in_months(self):
        duration = 3
        duration_type = 'year'
        duration_in_month = self.qualification_data_process.duration_in_months(
            duration=duration,
            duration_type=duration_type
        )
        self.assertEqual(duration_in_month, 36)

    def test_get_qualification_form_data(self):
        qualification_form_data = (
            self.qualification_data_process.qualification_form_data(
                form_data=self.wizard_form_data
            )
        )
        for key, qualification_data in qualification_form_data.items():
            self.assertEqual(
                qualification_data,
                self.wizard_form_data[key]
            )

    def test_update_qualification_data(self):
        self.qualification_data_process.process_data(
            form_data=self.wizard_form_data
        )
        updated_qualification = Qualification.objects.get(
            id=self.qualification.id
        )
        qualification_form_data = (
            self.qualification_data_process.qualification_form_data(
                form_data=self.wizard_form_data
            )
        )
        for key, qualification_data in qualification_form_data.items():
            qualification_value = getattr(updated_qualification, key)
            wizard_form_data = self.wizard_form_data[key]
            if qualification_value == '':
                qualification_value = None
            if wizard_form_data == '':
                wizard_form_data = None
            self.assertEqual(
                qualification_value,
                wizard_form_data
            )

    def test_add_subjects_to_qualification(self):
        self.qualification_data_process.add_subjects(
            form_data=self.wizard_form_data
        )
        subjects = QualificationEntranceRequirementSubject.objects.filter(
            qualification_id=self.qualification,
        )
        self.assertEqual(subjects.count(), 2)
        self.assertTrue(QualificationEntranceRequirementSubject.objects.filter(
            minimum_score=2
        ).exists())

    def test_add_requirements(self):
        requirement_form_data = {
            'min_nqf_level': 'LEVEL_1',
            'interview': True,
            'portfolio': True,
            'portfolio_comment': 'comment',
            'require_aps_score': False,
            'aps_calculator_link': 'http://test.com',
            'require_certain_subjects': False
        }
        self.qualification_data_process.add_requirements(
            requirement_form_data
        )
        requirements = Requirement.objects.filter(
            qualification=self.qualification.id
        )
        self.assertTrue(requirements.exists())
        requirement = requirements[0]
        for key, value in requirement_form_data.items():
            self.assertEqual(
                value,
                getattr(requirement, key)
            )

    def test_add_qualification_events(self):
        qualification_event_data = {
            'date_start': datetime.date(2018, 1, 1),
            'date_end': datetime.date(2019, 1, 1),
            'other_event': 'event',
            'event_date': datetime.date(2020, 1, 1)
        }
        self.qualification_data_process.add_qualification_event(
            qualification_event_data
        )
        events = QualificationEvent.objects.filter(
            qualification=self.qualification.id
        )
        self.assertTrue(events.exists())
        event = events[0]
        for key, value in qualification_event_data.items():
            self.assertEqual(
                value,
                getattr(event, key)
            )
