from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.test import TestCase
from match_all_check.models import *
from account.models import STAFF
import datetime as dt
# test models here


class BarcodeTest(TestCase):

    def create_barcode(self, barcode="D24.123456", comparisonId=1):
        self.user = User.objects.create_user(email="testemail@nhs.net",
                                             first_name="test",
                                             last_name="testington",
                                             username='testuser',
                                             password='12345')
        test_check = Check.objects.create(dateTime_check=dt.datetime(year=2024, month=3, day=23, hour=15, minute=23, second=10),
                                          barcode_count=2, user=self.user)
        return Barcode.objects.create(barcode=barcode, comparisonId=comparisonId, Check=test_check)

    def create_invalid_barcode(self, barcode="D24.1234", comparisonId=1):
        self.user = User.objects.create_user(email="testemail1@nhs.net",
                                             first_name="test1",
                                             last_name="testington1",
                                             username='testuser1',
                                             password='12345')
        test_check = Check.objects.create(dateTime_check=dt.datetime(year=2024, month=3, day=23, hour=15, minute=23, second=10),
                                          barcode_count=2, user=self.user)
        return Barcode.objects.create(barcode=barcode, comparisonId=comparisonId, Check=test_check)

    def test_barcode_creation(self):
        barcode = self.create_barcode()
        self.assertTrue(isinstance(barcode, Barcode))
        self.assertEqual(barcode.__str__(), f'{barcode.id}: {barcode.barcode}')
        self.assertEqual(barcode.comparisonId, 1)
        barcode = self.create_invalid_barcode()
        self.assertTrue(isinstance(barcode, Barcode))
        with self.assertRaises(ValidationError):
            barcode.full_clean()

class CheckTest(TestCase):

    def create_check(self, dateTime_check=dt.datetime(year=2024, month=3, day=23, hour=15, minute=23, second=10),
                     worksheet=123456, barcode_count=2):
        self.user = User.objects.create_user(email="testemail@nhs.net", first_name="test", last_name="testington",
                                                username='testuser', password='12345')
        return Check.objects.create(dateTime_check=dateTime_check, worksheet=worksheet,
                                    barcode_count=barcode_count, user=self.user)

    def test_check_creation(self):
        test_check = self.create_check()
        self.assertTrue(isinstance(test_check, Check))
        self.assertEqual(test_check.__str__(), f"{test_check.user}: {test_check.worksheet}, {test_check.dateTime_check.strftime("%H:%M:%S %d-%m-%Y")}")
