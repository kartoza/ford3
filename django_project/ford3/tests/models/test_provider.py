from django.test import TestCase
from ford3.tests.models.model_factories import ModelFactories
from ford3.models import Provider


class TestProvider(TestCase):

    def test_provider_description_save_and_read(self):
        new_provider = ModelFactories.get_provider_test_object()
        self.assertEqual(new_provider.__str__(), 'Object Test Name')

    def test_can_save_a_POST_request(self):
        response = self.client.post(
            '/ProviderForm/',
            data={
                'provider_tel': '082 123 3444'
            })
        self.assertEqual(Provider.objects.count(), 1)
        new_item = Provider.objects.first() # type: Provider
        self.assertEqual(new_item.telephone, '082 123 3444')
        self.assertIn('082 123 3444',
                      response.content.decode())

    def test_correct_template_used(self):
        response = self.client.post(
            '/ProviderForm/',
            data={
                'provider_tel': '082 123 3444'
            })
        self.assertTemplateUsed(response, 'provider_form.html')


