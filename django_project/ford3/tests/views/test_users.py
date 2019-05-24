from django.test import TestCase
from django.core.management import call_command
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission, User
from django.urls import reverse
from ford3.tests.models.model_factories import ModelFactories


class TestFixtures(TestCase):

    def test_province_group_fixture(self):
        call_command('loaddata', 'provinces_group')
        group_1 = Group.objects.get(pk=1)
        self.assertEqual(
            'Provinces',
            group_1.name,
            msg='Province group fixture failed')

    def test_provider_group_fixture(self):
        call_command('loaddata', 'providers_group')
        group_2 = Group.objects.get(pk=3)
        self.assertIn(
            'Providers',
            group_2.name,
            msg='Provider group fixture failed')

    def test_campus_group_fixture(self):
        call_command('loaddata', 'campus_group')
        group_3 = Group.objects.get(pk=2)
        self.assertIn(
            'Campus',
            group_3.name,
            msg='Campus group fixture failed')


class TestUsers(TestCase):

    def setUp(self):
        call_command('loaddata', 'provinces_group')
        call_command('loaddata', 'providers_group')
        call_command('loaddata', 'campus_group')

    # def test_province_user_(self):
    #     user = self.create_province_user()
    #
    #     self.fail(user)

    def test_province_user_can_create_provider_user(self):
        provider_user = {
            'username': 'new_provider',
            'password': 'temp',
            'email': 'temp2@temp.com'}
        user = self.create_province_user()
        url = reverse('create-provider-user')
        self.client.login(username='temp_province', password='temp')
        self.client.post(url, args=provider_user)
        self.assertIsInstance(
            get_user_model().objects.filter(username=user.username).first(),
            get_user_model())


    def create_temp_province_user(self):
        user = get_user_model().objects.create_user(
            'temp_province',
            'temp',
            'temp@temp.com')
        provinces_group: Group = Group.objects.get(name='Provinces')
        user.groups.add(provinces_group)
        return user

