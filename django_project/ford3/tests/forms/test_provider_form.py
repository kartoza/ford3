from django.test import TestCase
from ford3.forms.provider_form import ProviderForm, EMPTY_TEL_ERROR


class ProviderFormTest(TestCase):

    def test_form_validation_for_blank_items(self):
        form = ProviderForm(data={'telephone': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['telephone'], [EMPTY_TEL_ERROR])

    def test_provider_page_uses_provider_form(self):
        response = self.client.get('/ProviderForm/')
        self.assertIsInstance(response.context['form'], ProviderForm)

    def test_form_validation_for_max_length(self):
        form = ProviderForm(data={'telephone': '0821234123412341234'})
        self.assertFalse(form.is_valid())
