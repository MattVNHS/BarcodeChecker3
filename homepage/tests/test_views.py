from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from match_all_check.views import *
from match_pair_check.views import *
from homepage.views import *
# test views here


class HomepageViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(email="testemail1@nhs.net",
                                             first_name="test1",
                                             last_name="testington1",
                                             username='testuser1',
                                             password='12345')
        self.client.login(username='testuser1', password='12345')
        self.url = reverse('home')

    def test_homepage_get_context(self):
        # Test the page loads correctly with the correct forms

        response = self.client.get(self.url, follow=True)

        self.assertEqual(response.resolver_match.func, home_screen_view)
        self.assertTemplateUsed(response, 'homepage/home.html')
        self.assertEqual(response.status_code, 200)

    def test_homepage_MatchAllCheck_post_request(self):
        # Test a Post request loads a MatchAllCheck page

        response = self.client.post(self.url, data={'barcode_count': 2, 'url_name': 'MatchAllView'}, follow=True)

        self.assertIs(response.resolver_match.func.view_class, MatchAllView)
        self.assertEqual(response.context['barcodes'].extra, 2)
        self.assertTemplateUsed(response, 'match_all_check/match_all_check.html')
        self.assertEqual(response.status_code, 200)

    def test_homepage_MatchAllWorksheetCheck_post_request(self):
        # Test a Post request loads a MatchAllWorksheetCheck page

        response = self.client.post(self.url, data={'barcode_count': 2, 'url_name': 'WorksheetMatchAllView'}, follow=True)

        self.assertIs(response.resolver_match.func.view_class, WorksheetMatchAllView)
        self.assertEqual(response.context['barcodes'].extra, 2)
        self.assertTemplateUsed(response, 'match_all_check/match_all_check.html')
        self.assertEqual(response.status_code, 200)

    def test_homepage_MatchPairCheck_post_request(self):
        # Test a Post request loads a MatchPairCheck page

        response = self.client.post(self.url, data={'barcode_count': 2, 'url_name': 'WorksheetMatchPairView'}, follow=True)

        self.assertIs(response.resolver_match.func.view_class, WorksheetMatchPairView)
        self.assertEqual(response.context['barcodes'].extra, 2)
        self.assertTemplateUsed(response, 'match_all_check/match_all_check.html')
        self.assertEqual(response.status_code, 200)

