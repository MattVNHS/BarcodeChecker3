from django.contrib.auth.models import User
from django.test import TestCase, TransactionTestCase
from django.urls import reverse
from account.views import *
from homepage.views import *

from account.models import *
# test views here


# class HomepageViewTest(TestCase):
#
#     def setUp(self):
#         # self.user = User.objects.create_user(email="testemail1@nhs.net",
#         #                                      first_name="test1",
#         #                                      last_name="testington1",
#         #                                      username='testuser1',
#         #                                      password='12345')
#         #self.client.login(username='testuser1', password='12345')
#         self.url = reverse('login')
#
#     def test_login_get_context(self):
#         # Test the page loads correctly with the correct forms
#
#         response = self.client.get(self.url, follow=True)
#
#         self.assertIs(response.resolver_match.func.view_class, Login)
#         self.assertTemplateUsed(response, 'account/login.html')
#         self.assertEqual(response.status_code, 200)
#
#     def test_invalid_login(self):
#         # Test the page loads correctly with the correct forms
#
#         response = self.client.post(self.url, data={'txtUsername': '', 'txtPassword': ''}, follow=True)
#
#         self.assertIs(response.resolver_match.func.view_class, Login)
#         self.assertTemplateUsed(response, 'account/login.html')
#         self.assertEqual(response.status_code, 200)
#
#     def test_valid_login(self):
#         # Test the page loads correctly with the correct forms
#
#         response = self.client.post(self.url, data={'txtUsername': 'testuser1', 'txtPassword': '12345'}, follow=True)
#
#        # self.assertEqual(response.resolver_match.func, home_screen_view)
#         self.assertTemplateUsed(response, 'homepage/home.html')
#         self.assertEqual(response.status_code, 200)


class HomepageViewTest(TransactionTestCase):

    def setUp(self):
        self.user = User.objects.create_user(email="testemail1@nhs.net",
                                             first_name="test1",
                                             last_name="testington1",
                                             username='testuser1',
                                             password='12345')
        # self.client.login(username='testuser1', password='12345')
        self.url = reverse('login')
    def test_succesful_login(self):
        # Test the page loads correctly with the correct forms
        self.user = None
        response = self.client.post(self.url, data={'txtUsername': 'testuser1', 'txtPassword': '12345'}, follow=True)

        self.assertEqual(response.resolver_match.func, home_screen_view)
        self.assertTemplateUsed(response, 'homepage/home.html')
        self.assertEqual(response.status_code, 200)

    def test_invalid_login(self):
        # Test the page loads correctly with the correct forms
        self.user = None
        response = self.client.post(self.url, data={'txtUsername': 'incorrect_username',
                                                    'txtPassword': 'incorrect_password'}, follow=True)

        self.assertIs(response.resolver_match.func.view_class, Login)
        self.assertTemplateUsed(response, 'account/login.html')
        self.assertEqual(response.status_code, 200)
    # def test_homepage_MatchAllCheck_post_request(self):
    #     # Test a Post request loads a MatchAllCheck page
    #
    #     response = self.client.post(self.url, data={'barcode_count': 2, 'url_name': 'MatchAllCheckView'}, follow=True)
    #
    #     self.assertIs(response.resolver_match.func.view_class, MatchAllCheckView)
    #     self.assertEqual(response.context['barcodes'].extra, 2)
    #     self.assertTemplateUsed(response, 'match_all_check/match_all_check.html')
    #     self.assertEqual(response.status_code, 200)
    #
    # def test_homepage_MatchAllWorksheetCheck_post_request(self):
    #     # Test a Post request loads a MatchAllWorksheetCheck page
    #
    #     response = self.client.post(self.url, data={'barcode_count': 2, 'url_name': 'MatchAllCheckWorksheetView'}, follow=True)
    #
    #     self.assertIs(response.resolver_match.func.view_class, MatchAllCheckWorksheetView)
    #     self.assertEqual(response.context['barcodes'].extra, 2)
    #     self.assertTemplateUsed(response, 'match_all_check/match_all_check.html')
    #     self.assertEqual(response.status_code, 200)
    #
    # def test_homepage_MatchPairCheck_post_request(self):
    #     # Test a Post request loads a MatchPairCheck page
    #
    #     response = self.client.post(self.url, data={'barcode_count': 2, 'url_name': 'MatchPairCheckView'}, follow=True)
    #
    #     self.assertIs(response.resolver_match.func.view_class, MatchPairCheckView)
    #     self.assertEqual(response.context['barcodes'].extra, 2)
    #     self.assertTemplateUsed(response, 'match_all_check/match_all_check.html')
    #     self.assertEqual(response.status_code, 200)

