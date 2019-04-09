from django.test import TestCase
from django.urls import reverse
from ford3.tests.models.model_factories import ModelFactories


class TestProvider(TestCase):

    def setUp(self):
        self.new_provider = ModelFactories.get_provider_test_object()

    def test_provider_description_save_and_read(self):

        self.assertEqual(str(self.new_provider), 'Object Test Name')

    def test_is_new_provider(self):
        self.assertTrue(self.new_provider.is_new_provider)

        campus = ModelFactories.get_campus_test_object()
        campus.provider_id = self.new_provider.id
        campus.save()

        self.assertEqual(self.new_provider.id, campus.provider_id)

        self.assertFalse(self.new_provider.is_new_provider)

    def test_correct_GET_template_used(self):
        url = reverse(
                'edit-provider',
                kwargs={
                    'provider_id': self.new_provider.id})
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'provider_form.html')
