from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from match_all_check.views import *
from homepage.views import *
# test views here


class Match_all_checkViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(email="testemail1@nhs.net",
                                             first_name="test1",
                                             last_name="testington1",
                                             username='testuser1',
                                             password='12345')
        self.client.login(username='testuser1', password='12345')
        self.url = reverse('MatchAllCheckView', kwargs={'barcode_count': 2})

    def test_get_context_data_get_request(self):
        # Test the page loads correctly with the right number of barcode forms.
        # if self.request.POST is tested via form_invalid and form valid tests
        # (these are integration tests not unit tests)
        response = self.client.get(self.url, follow=True)

        self.assertIs(response.resolver_match.func.view_class, MatchAllCheckView)
        self.assertTemplateUsed(response, 'match_all_check/match_all_check.html')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['barcodes'].extra, 2)

    def test_invalid_barcode(self):
        form_data = {'matchallbarcode_set-TOTAL_FORMS': '2', 'matchallbarcode_set-INITIAL_FORMS': '0',
                     'matchallbarcode_set-MIN_NUM_FORMS': '0', 'matchallbarcode_set-MAX_NUM_FORMS': '1000',
                     'matchallbarcode_set-0-barcode': 'D24.654', 'matchallbarcode_set-1-barcode': 'D24.654321'}

        response = self.client.post(self.url, data=form_data, follow=True)
        message = list(response.context.get('messages'))[0]
        barcode_form = response.context.get('barcodes')

        self.assertIs(response.resolver_match.func.view_class, MatchAllCheckView)
        self.assertEqual(message.tags, "warning")
        self.assertFalse(barcode_form.is_valid())
        self.assertFormSetError(barcode_form, field='barcode', errors='invalid lab number entered',
                                form_index=0)
        self.assertTemplateUsed(response, 'match_all_check/match_all_check.html')
        self.assertEqual(response.status_code, 200)

    def test_check_pass(self):
        form_data = {'matchallbarcode_set-TOTAL_FORMS': '2', 'matchallbarcode_set-INITIAL_FORMS': '0',
                     'matchallbarcode_set-MIN_NUM_FORMS': '0', 'matchallbarcode_set-MAX_NUM_FORMS': '1000',
                     'matchallbarcode_set-0-barcode': 'D24.654321', 'matchallbarcode_set-1-barcode': 'D24.654321'}

        response = self.client.post(self.url, data=form_data, follow=True)
        message = list(response.context.get('messages'))[0]

        self.assertEqual(message.tags, "success")
        self.assertTrue("Check Pass" in message.message)
        self.assertEqual(response.resolver_match.func, home_screen_view)
        self.assertRedirects(response, '/')
        self.assertTemplateUsed(response, 'homepage/home.html')
        self.assertEqual(response.status_code, 200)


    def test_check_fail(self):
        form_data = {'matchallbarcode_set-TOTAL_FORMS': '2', 'matchallbarcode_set-INITIAL_FORMS': '0',
                     'matchallbarcode_set-MIN_NUM_FORMS': '0', 'matchallbarcode_set-MAX_NUM_FORMS': '1000',
                     'matchallbarcode_set-0-barcode': 'D24.111111', 'matchallbarcode_set-1-barcode': 'D24.654321'}

        response = self.client.post(self.url, data=form_data, follow=True)
        message = list(response.context.get('messages'))[0]

        self.assertEqual(message.tags, "warning")
        self.assertTrue("Check Failed - Barcodes do not match" in message.message)
        self.assertEqual(response.resolver_match.func, home_screen_view)
        self.assertRedirects(response, '/')
        self.assertTemplateUsed(response, 'homepage/home.html')
        self.assertEqual(response.status_code, 200)


class Match_all_check_worksheetViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(email="testemail1@nhs.net",
                                             first_name="test1",
                                             last_name="testington1",
                                             username='testuser1',
                                             password='12345')
        self.client.login(username='testuser1', password='12345')
        self.url = reverse('MatchAllCheckWorksheetView', kwargs={'barcode_count': 2})

    def test_get_context_data_get_request(self):
        # Test the page loads correctly with the right number of barcode forms.
        # if self.request.POST is tested via form_invalid and form valid tests
        # (these are integration tests not unit tests)
        response = self.client.get(self.url, follow=True)

        self.assertIs(response.resolver_match.func.view_class, MatchAllCheckWorksheetView)
        self.assertTemplateUsed(response, 'match_all_check/match_all_check.html')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['barcodes'].extra, 2)

    def test_invalid_barcode(self):
        form_data = {'worksheet': '123456',
                     'matchallbarcode_set-TOTAL_FORMS': '2', 'matchallbarcode_set-INITIAL_FORMS': '0',
                     'matchallbarcode_set-MIN_NUM_FORMS': '0', 'matchallbarcode_set-MAX_NUM_FORMS': '1000',
                     'matchallbarcode_set-0-barcode': 'D24.654', 'matchallbarcode_set-1-barcode': 'D24.654321'}

        response = self.client.post(self.url, data=form_data, follow=True)
        message = list(response.context.get('messages'))[0]
        barcode_form = response.context.get('barcodes')

        self.assertIs(response.resolver_match.func.view_class, MatchAllCheckWorksheetView)
        self.assertEqual(message.tags, "warning")
        self.assertFalse(barcode_form.is_valid())
        self.assertFormSetError(barcode_form, field='barcode', errors='invalid lab number entered',
                                form_index=0)
        self.assertIs(response.resolver_match.func.view_class, MatchAllCheckWorksheetView)
        self.assertTemplateUsed(response, 'match_all_check/match_all_check.html')
        self.assertEqual(response.status_code, 200)

    def test_invalid_worksheet(self):
        form_data = {'worksheet': '1234',
                     'matchallbarcode_set-TOTAL_FORMS': '2', 'matchallbarcode_set-INITIAL_FORMS': '0',
                     'matchallbarcode_set-MIN_NUM_FORMS': '0', 'matchallbarcode_set-MAX_NUM_FORMS': '1000',
                     'matchallbarcode_set-0-barcode': 'D24.654321', 'matchallbarcode_set-1-barcode': 'D24.654321'}

        response = self.client.post(self.url, data=form_data, follow=True)
        message = list(response.context.get('messages'))[0]
        form = list(response.context.get('form'))[0]

        self.assertEqual(message.tags, "warning")
        self.assertTrue("invalid worksheet entered" in form.errors)
        self.assertIs(response.resolver_match.func.view_class, MatchAllCheckWorksheetView)
        self.assertTemplateUsed(response, 'match_all_check/match_all_check.html')
        self.assertEqual(response.status_code, 200)


    def test_check_pass(self):

        form_data = {'worksheet': '123456',
                     'matchallbarcode_set-TOTAL_FORMS': '2', 'matchallbarcode_set-INITIAL_FORMS': '0',
                     'matchallbarcode_set-MIN_NUM_FORMS': '0', 'matchallbarcode_set-MAX_NUM_FORMS': '1000',
                     'matchallbarcode_set-0-barcode': 'D24.654321', 'matchallbarcode_set-1-barcode': 'D24.654321'}

        response = self.client.post(self.url, data=form_data, follow=True)
        message = list(response.context.get('messages'))[0]

        self.assertEqual(message.tags, "success")
        self.assertTrue("Check Pass" in message.message)
        self.assertEqual(response.resolver_match.func, home_screen_view)
        self.assertRedirects(response, '/')
        self.assertTemplateUsed(response, 'homepage/home.html')
        self.assertEqual(response.status_code, 200)

    def test_check_fail(self):
        form_data = {'worksheet': '123456',
                     'matchallbarcode_set-TOTAL_FORMS': '2', 'matchallbarcode_set-INITIAL_FORMS': '0',
                     'matchallbarcode_set-MIN_NUM_FORMS': '0', 'matchallbarcode_set-MAX_NUM_FORMS': '1000',
                     'matchallbarcode_set-0-barcode': 'D24.111111', 'matchallbarcode_set-1-barcode': 'D24.654321'}

        response = self.client.post(self.url, data=form_data, follow=True)
        message = list(response.context.get('messages'))[0]

        self.assertEqual(message.tags, "warning")
        self.assertTrue("Check Failed - Barcodes do not match" in message.message)
        self.assertEqual(response.resolver_match.func, home_screen_view)
        self.assertRedirects(response, '/')
        self.assertTemplateUsed(response, 'homepage/home.html')
        self.assertEqual(response.status_code, 200)

