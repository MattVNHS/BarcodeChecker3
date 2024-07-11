from django.contrib import auth
from django.contrib.auth.models import User
from django.test import TestCase
from account.views import *
from homepage.views import *


class HomepageViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(email="testemail1@nhs.net",
                                             first_name="test1",
                                             last_name="testington1",
                                             username='testuser1',
                                             password='12345')
        self.client.login(username='testuser1', password='12345')
        self.url = reverse('login')

    def test_successful_login(self):
        # Test the page loads correctly with the correct forms
        self.user = None
        response = self.client.post(self.url, data={'txtUsername': 'testuser1', 'txtPassword': '12345'}, follow=True)
        user = auth.get_user(self.client)

        self.assertEqual(user.is_authenticated, True)
        self.assertEqual(response.resolver_match.func, home_screen_view)
        self.assertTemplateUsed(response, 'homepage/home.html')
        self.assertEqual(response.status_code, 200)

    def test_successful_logout(self):
        # Test logging out
        response = self.client.get(reverse('logout'),  follow=True)
        user = auth.get_user(self.client)

        self.assertEqual(user.is_authenticated, False)
        self.assertIs(response.resolver_match.func.view_class, Login)
        self.assertTemplateUsed(response, 'account/login.html')
        self.assertEqual(response.status_code, 200)

    def test_invalid_login(self):
        # Test the page loads correctly with the correct forms
        self.client.logout()
        response = self.client.post(self.url, data={'txtUsername': 'incorrect_username',
                                                    'txtPassword': 'incorrect_password'}, follow=True)

        user = auth.get_user(self.client)

        self.assertEqual(user.is_authenticated, False)
        self.assertIs(response.resolver_match.func.view_class, Login)
        self.assertTemplateUsed(response, 'account/login.html')
        self.assertEqual(response.status_code, 200)