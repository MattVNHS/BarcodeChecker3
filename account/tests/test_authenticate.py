from django.contrib.auth import authenticate
from django.test import TestCase
from django.urls import reverse

from account.authentication import *


class AuthenticationTest(TestCase):

    def setUp(self):
        User.objects.filter(username='CRT0').delete()
        self.user = User.objects.create_user(email="testemail1@nhs.net",
                                             first_name="test1",
                                             last_name="testington1",
                                             username='testuser1',
                                             password='12345')
        self.client.login(username='testuser1', password='12345')
        self.url = reverse('login')

    def test_default_authentication(self):
        # Test authenticate returns a User from PostgreSQL (not Shire)

        user = authenticate(username='testuser1', password='12345')
        self.assertIsInstance(user, User)

    def test_invalid_authentication(self):
        # Test authenticate returns a None from PostgreSQL (not Shire)

        user = authenticate(username='test', password=None)
        self.assertIsNone(user)
        user = authenticate(username=None, password='12345')
        self.assertIsNone(user)
