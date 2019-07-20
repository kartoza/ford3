from django.urls import reverse
from django.test import TestCase
from ford3.tests.models.model_factories import ModelFactories
from ford3.models.qualification import Qualification
from ford3.models.user import User
from ford3.models.people_group import PeopleGroup
from ford3.views.qualification_wizard import QualificationFormWizardDataProcess


# @override_settings(
#     STATICFILES_STORAGE='pipeline.storage.NonPackagingPipelineStorage',
#     PIPELINE_ENABLED=False)
class TestQualificationWizard(TestCase):
    fixtures = [
        'groups',
        'sa_provinces',
        'test_province_users',
        'test_provider_users',
        'test_campus_users',
        'test_providers',
        'people_groups'
    ]

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
        'occupations_ids': '',
        'critical_skill': '',
        'green_occupation': '',
        'high_demand_occupation': '',
        'subject_list': '1,2',
        'minimum_score_list': '-1,2'
    }

    def setUp(self):
        self.qualification = ModelFactories.get_qualification_test_object()
        self.wizard_url = reverse(
            'edit-qualification',
            args=(
                self.qualification.campus.provider.id,
                self.qualification.campus.id,
                self.qualification.id))
        self.user = User.objects.get(pk=3)
        self.user.set_password(self.user.password)
        self.qualification_data_process = QualificationFormWizardDataProcess(
            qualification=self.qualification,
            edited_by=self.user
        )

    def test_validate_data(self):
        self.assertTrue(True)

    def test_initial_call(self):
        # should be redirected before logged in
        response = self.client.get(self.wizard_url)
        self.assertEqual(response.status_code, 302)
        self.client.login(email=self.user.email, password='password')
        # should be succeed after logged in
        response = self.client.get(self.wizard_url, follow=True)
        self.assertEqual(response.status_code, 200)

        # wizard = response.context['wizard']
        # self.assertEqual(response.status_code, 200)
        # self.assertEqual(wizard['steps'].current, 'qualification-details')
        # self.assertEqual(wizard['steps'].step0, 0)
        # self.assertEqual(wizard['steps'].step1, 1)
        # self.assertEqual(
        # wizard['steps'].last, 'qualification-important-dates')
        # self.assertEqual(wizard['steps'].prev, None)
        # self.assertEqual(wizard['steps'].next, 'qualification-duration')
        # self.assertEqual(wizard['steps'].count, 5)

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
        pass

    def test_add_requirements(self):
        requirement_form_data = {
            'min_nqf_level': 'LEVEL_1',
            'interview': True,
            'portfolio': True,
            'assessment': True,
            'assessment_comment': 'assessment comment',
            'portfolio_comment': 'comment',
            'require_certain_subjects': False,
            'require_aps_score': False,
            'aps_calculator_link': '',
            'admission_point_scores': '(1 12),(2 2),(3 43)'
        }

        self.qualification_data_process.add_or_update_requirements(
            requirement_form_data
        )

        requirement = self.qualification.requirement
        for key, value in requirement_form_data.items():
            self.assertEqual(
                value,
                getattr(requirement, key)
            )

        # key "admission_point_scores" is removed from requirement_form_data
        # require_aps_score is set to False
        # it should return [0, 0, 0]
        self.assertEqual([
            aps['value']
            for aps in requirement.admission_point_scores
        ], [0] * 3)

        # update the admission point scores
        requirement_form_data['require_aps_score'] = True
        requirement_form_data['aps_calculator_link'] = 'http://bbc.com'

        requirement_form_data['admission_point_scores'] = ','.join([
            f'({pg.id} 1000)'
            for pg in PeopleGroup.objects.all()
        ])

        self.qualification_data_process.add_or_update_requirements(
            requirement_form_data)

        requirement = self.qualification.requirement

        self.assertEqual([
            aps['value']
            for aps in requirement.admission_point_scores
        ], [1000] * 3)

        self.assertTrue(requirement.require_aps_score)
        self.assertEqual(requirement.aps_calculator_link, 'http://bbc.com')
