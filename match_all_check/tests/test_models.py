from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.test import TestCase
from match_all_check.models import *
from account.models import STAFF
import datetime as dt
# test models here

class MatchAllCheckTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(email="testemail1@nhs.net",
                                             first_name="test1",
                                             last_name="testington1",
                                             username='testuser1',
                                             password='12345')
        self.client.login(username='testuser1', password='12345')

    def create_check(self, check_time=dt.datetime.now()):
        test_check = MatchAllCheck.objects.create(dateTime_check=check_time, worksheet='123456', user=self.user)
        MatchAllBarcode.objects.create(barcode='D24.123456', Check=test_check)
        MatchAllBarcode.objects.create(barcode='D24.123456', Check=test_check)
        return test_check

    def test_is_instance(self):
        test_check = self.create_check()
        self.assertIsInstance(test_check, MatchAllCheck)

    def test_check_pass(self):
        test_check = self.create_check()
        test_check.checkPassFail()
        self.assertTrue(test_check.check_pass)

    def test_check_fail(self):
        test_check = self.create_check()
        MatchAllBarcode.objects.create(barcode='D24.111111', Check=test_check)
        self.assertFalse(test_check.check_pass)

    def test_check_str(self):
        test_check = self.create_check()
        self.assertEqual(test_check.__str__(),
                         f"{test_check.user}: {test_check.worksheet}, {test_check.dateTime_check.strftime("%H:%M:%S %d-%m-%Y")}")


class MatchPairCheckTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(email="testemail1@nhs.net",
                                             first_name="test1",
                                             last_name="testington1",
                                             username='testuser1',
                                             password='12345')
        self.client.login(username='testuser1', password='12345')

    def create_check(self, check_time=dt.datetime.now()):
        test_check = MatchPairCheck.objects.create(dateTime_check=check_time, worksheet='123456', user=self.user)
        barcode1 = MatchPairBarcode.objects.create(barcode='D24.123456', Check=test_check)
        barcode2 = MatchPairBarcode.objects.create(barcode='D24.123456', Check=test_check, comparisonId = barcode1)
        barcode1.comparisonId = barcode2
        barcode1.save()
        barcode2.save()
        test_check.save()
        return test_check

    def test_is_instance(self):
        test_check = self.create_check()
        self.assertIsInstance(test_check, MatchPairCheck)

    def test_check_pass(self):
        test_check = self.create_check()
        test_check.checkPassFail()
        self.assertTrue(test_check.check_pass)

    def test_check_fail(self):
        test_check = self.create_check()
        barcode3 = MatchPairBarcode.objects.create(barcode='D24.123456', Check=test_check)
        barcode4 = MatchPairBarcode.objects.create(barcode='D24.111111', Check=test_check, comparisonId=barcode3)
        barcode3.comparisonId = barcode4
        barcode3.save()
        barcode4.save()
        test_check.checkPassFail()
        self.assertFalse(test_check.check_pass)

    def test_check_str(self):
        test_check = self.create_check()
        self.assertEqual(test_check.__str__(),
                         f"{test_check.user}: {test_check.worksheet}, {test_check.dateTime_check.strftime("%H:%M:%S %d-%m-%Y")}")


class BarcodeTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email="testemail1@nhs.net",
                                             first_name="test1",
                                             last_name="testington1",
                                             username='testuser1',
                                             password='12345')
        self.client.login(username='testuser1', password='12345')
        self.match_all_check = MatchAllCheck.objects.create(dateTime_check=dt.datetime.now(),
                                                            worksheet='123456', user=self.user)
        self.match_pair_check =MatchPairCheck.objects.create(dateTime_check=dt.datetime.now(),
                                                             worksheet='123456', user=self.user)

    def create_match_all_barcode(self):
        return MatchAllBarcode.objects.create(barcode='D24.123456', Check=self.match_all_check)

    def test_match_all_barcode_is_instance(self):
        test_barcode = self.create_match_all_barcode()
        self.assertIsInstance(test_barcode, MatchAllBarcode)
        self.assertIsInstance(test_barcode.Check, MatchAllCheck)

    def test_match_all_barcode_str(self):
        test_barcode = self.create_match_all_barcode()
        self.assertEqual(test_barcode.__str__(), f"{test_barcode.pk}: {test_barcode.barcode}")


    def create_match_pair_barcodes(self):
        barcode1 = MatchPairBarcode.objects.create(barcode='D24.123456', Check=self.match_pair_check)
        barcode2 = MatchPairBarcode.objects.create(barcode='D24.123456', Check=self.match_pair_check,
                                                   comparisonId=barcode1)
        barcode1.comparisonId = barcode2
        barcode1.save()
        barcode2.save()
        self.match_pair_check.save()
        return barcode1, barcode2

    def test_match_pair_barcode_is_instance(self):
        test_barcode1, test_barcode2 = self.create_match_pair_barcodes()
        self.assertIsInstance(test_barcode1, MatchPairBarcode)
        self.assertIsInstance(test_barcode1.Check, MatchPairCheck)
        self.assertEqual(test_barcode1.comparisonId, test_barcode2)
        self.assertEqual(test_barcode2.comparisonId, test_barcode1)

    def test_match_pair_barcode_str(self):
        test_barcode1, _ = self.create_match_pair_barcodes()
        self.assertEqual(test_barcode1.__str__(), f"{test_barcode1.pk}: {test_barcode1.barcode}")



