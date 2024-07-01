from django.contrib.auth.models import User
from django.test import TestCase

from match_all_check.views import *
from match_all_check.forms import *
from django.urls import reverse

from django.contrib.messages import get_messages

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
        # if self.request.POST is tested via form_invalid and form valid tests (these are integration tests not unit tests)
        response = self.client.get(self.url, follow=True)
        self.assertTemplateUsed(response, 'match_all_check/match_all_check.html')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['barcodes'].extra, 2)

    # def test_form_invalid_lab_number(self):
    #     # Test invalid barcode entered
    #     form_data = {'csrfmiddlewaretoken': ['UP7MtIXmLtqR22KIvMb0INCnx3ns09rfDXDEpdyllZimr8ppMMUll5HHCFqzFwDg'],
    #                  'matchallbarcode_set-TOTAL_FORMS': ['2'], 'matchallbarcode_set-INITIAL_FORMS': ['0'],
    #                  'matchallbarcode_set-MIN_NUM_FORMS': ['0'], 'matchallbarcode_set-MAX_NUM_FORMS': ['1000'],
    #                  'matchallbarcode_set-0-barcode': ['D24.6543'], 'matchallbarcode_set-0-id': [''],'matchallbarcode_set-0-Check': [''],
    #                  'matchallbarcode_set-1-barcode': ['D24.654321'], 'matchallbarcode_set-1-id': [''], 'matchallbarcode_set-1-Check': ['']}
    #
    #     response = self.client.post(self.url, data=form_data, follow=True)
    #
    #     self.assertFalse(response.context['barcodes'].is_valid())
    #     self.assertFormSetError(response.context['barcodes'], field='barcode', errors='invalid lab number entered', form_index=0)
    #     self.assertTemplateUsed(response, 'match_all_check/match_all_check.html')
    #     self.assertEqual(response.status_code, 200)

    def test_check_pass(self):

        form_data = {'matchallbarcode_set-TOTAL_FORMS': '2', 'matchallbarcode_set-INITIAL_FORMS': '0',
                     'matchallbarcode_set-MIN_NUM_FORMS': '0', 'matchallbarcode_set-MAX_NUM_FORMS': '1000',
                     'matchallbarcode_set-0-barcode': 'D24.654321', 'matchallbarcode_set-1-barcode': 'D24.654321'}

        response = self.client.post(self.url, data=form_data, follow=True)
        message = list(response.context.get('messages'))[0]

        self.assertEqual(message.tags, "success")
        self.assertTrue("Check Pass" in message.message)
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
        # if self.request.POST is tested via form_invalid and form valid tests (these are integration tests not unit tests)
        response = self.client.get(self.url, follow=True)
        self.assertTemplateUsed(response, 'match_all_check/match_all_check.html')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['barcodes'].extra, 2)

    def test_check_pass(self):

        form_data = {'matchallbarcode_set-TOTAL_FORMS': '2', 'matchallbarcode_set-INITIAL_FORMS': '0',
                     'matchallbarcode_set-MIN_NUM_FORMS': '0', 'matchallbarcode_set-MAX_NUM_FORMS': '1000',
                     'matchallbarcode_set-0-barcode': 'D24.654321', 'matchallbarcode_set-1-barcode': 'D24.654321'}

        response = self.client.post(self.url, data=form_data, follow=True)
        message = list(response.context.get('messages'))[0]

        self.assertEqual(message.tags, "success")
        self.assertTrue("Check Pass" in message.message)
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
        self.assertRedirects(response, '/')
        self.assertTemplateUsed(response, 'homepage/home.html')
        self.assertEqual(response.status_code, 200)

