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

    def test_provider_being_removed(self):
        remove_url = reverse(
            'remove-provider',
            args=[
                self.campus2.provider.id])
        show_provider_url = reverse(
            'show-provider',
            args=[
                self.campus2.provider.id])
        edit_provider_url = reverse(
            'edit-provider',
            args=[
                self.campus2.provider.id])

        # check if the provider exist before delete
        show_provider_response = self.client.get(show_provider_url)
        self.assertEquals(show_provider_response.status_code, 200)

        edit_provider_response = self.client.get(edit_provider_url)
        self.assertEquals(edit_provider_response.status_code, 200)

        # delete the provider
        self.client.get(remove_url)

        # check if the provider can't no longer be found
        show_provider_response = self.client.get(show_provider_url)
        self.assertEquals(show_provider_response.status_code, 404)

        edit_provider_response = self.client.get(edit_provider_url)
        self.assertEquals(edit_provider_response.status_code, 404)
