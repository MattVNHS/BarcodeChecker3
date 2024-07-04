from homepage.forms import *
from django.test import TestCase
from django.contrib.auth.models import User


class FormsTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(email="testemail1@nhs.net",
                                             first_name="test1",
                                             last_name="testington1",
                                             username='testuser1',
                                             password='12345')
        self.client.login(username='testuser1', password='12345')

    def test_MatchAllForm_valid(self):
        test_form = MatchAllForm(data={'barcode_count': 2, 'url_name': 'MatchAllCheckView'})

        self.assertTrue(test_form.is_valid())

    def test_MatchAllWorksheetForm_valid(self):
        test_form = MatchAllWorksheetForm(data={'barcode_count': 2, 'url_name': 'MatchAllCheckWorksheetView'})

        self.assertTrue(test_form.is_valid())

    def test_MatchPairForm_valid(self):
        test_form = MatchPairForm(data={'barcode_count': 8, 'url_name': 'MatchPairCheckView'})

        self.assertTrue(test_form.is_valid())