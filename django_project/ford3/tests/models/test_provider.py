from django.test import TestCase
from ford3.tests.models.model_factories import ModelFactories
from ford3.models import Provider



class TestProvider(TestCase):

    def test_provider_description_save_and_read(self):
        new_provider = ModelFactories.get_provider_test_object()
        self.assertEqual(new_provider.__str__(), 'Object Test Name')

    def test_correct_GET_template_used(self):
        response = self.client.get(
            '/providers')
        self.assertTemplateUsed(response, 'provider_form.html')

    def test_only_saves_items_when_necessary(self):
        self.client.get('/providers')
        self.assertEqual(Provider.objects.count(), 0)
