from django.urls import reverse
from django.test import TestCase
from ford3.tests.models.model_factories import ModelFactories


class TestProvider(TestCase):
    def setUp(self):
        self.provider1 = ModelFactories.get_provider_test_object(new_id=1000)
        self.campus1 = ModelFactories.get_campus_test_object(new_id=3000)
        self.campus2 = ModelFactories.get_campus_test_object(new_id=4000)
        self.qualification1 = \
            ModelFactories.get_qualification_test_object(new_id=5000)

    def test_existed_show_provider_with_campus(self):
        url = reverse('show-provider', args=[self.campus1.provider.id])

        response = self.client.get(url)
        # should go to the show provider page
        self.assertEquals(response.status_code, 200)

    def test_existed_show_provider_without_campus(self):
        # provider1 = ModelFactories.get_provider_test_object(new_id=1)
        url = reverse('show-provider', args=[self.provider1.id])

        response = self.client.get(url)
        # should redirect to the edit provider page
        self.assertEquals(response.status_code, 302)

    def test_non_exist_show_provider(self):
        url = reverse('show-provider', args=[1001])

        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)
