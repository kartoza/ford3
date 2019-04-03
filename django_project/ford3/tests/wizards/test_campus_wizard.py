# from django.test import TestCase
# from django.test.utils import override_settings
# from ford3.tests.models.model_factories import ModelFactories
# from ford3.views.campus_wizard import CampusFormWizard
#
#
# @override_settings(
#     STATICFILES_STORAGE='pipeline.storage.NonPackagingPipelineStorage',
#     PIPELINE_ENABLED=False)
# class TestCampusWizard(TestCase):
#
#     def setUp(self):
#         self.campus = ModelFactories.get_campus_test_object(
#             new_id=1
#         )
#
#         self.wizard_url = '/'.join([
#             '/ford3/providers/{}'.format(
#                 self.campus.campus.provider.id),
#             'campus/{}'.format(
#                 self.campus.campus.id),
#             'campuss/{}/edit'.format(
#                 self.campus.id)])
#
#         self.event_1 = ModelFactories.get_campus_event_test_object(
#             new_id=1
#         )
#         self.event_2 = ModelFactories.get_campus_event_test_object(
#             new_id=2
#         )
#
#         self.campus_data_process = CampusFormWizard(campus=self.campus)
#
#     def test_initial_call(self):\
#
#
#     def test_add_events_to_campus(self):
#         # Check if event was added
#
#
