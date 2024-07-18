from django.test import TestCase
from match_pair_check.forms import *
from match_all_check.models import MatchPairCheck
from django.contrib.auth.models import User


class FormsetTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(email="testemail1@nhs.net",
                                             first_name="test1",
                                             last_name="testington1",
                                             username='testuser1',
                                             password='12345')
        self.client.login(username='testuser1', password='12345')

        self.data = {
            'matchpairbarcode_set-TOTAL_FORMS': '2',
            'matchpairbarcode_set-INITIAL_FORMS': '0',
            'matchpairbarcode_set-MIN_NUM_FORMS': '0',
            'matchpairbarcode_set-MAX_NUM_FORMS': '1000'
        }

    def create_formset(self):
        check = MatchPairCheck.objects.first()
        formset = inlineformset_factory(
            MatchPairCheck, MatchPairBarcode, can_delete_extra=False, form=BarcodePairForm,
            formset=BaseInlineCheckFormSet, extra=0)
        test_formset = formset(instance=check, data=self.data)
        return test_formset

    def test_valid_barcode(self):
        self.data['matchpairbarcode_set-0-barcode'] = 'D24.654321'
        self.data['matchpairbarcode_set-1-barcode'] = 'D24.654321'

        test_formset = self.create_formset()

        self.assertTrue(test_formset.is_valid())

    def test_invalid_barcode(self):
        self.data['matchpairbarcode_set-0-barcode'] = 'D24.6543'
        self.data['matchpairbarcode_set-1-barcode'] = 'D24.654321'

        test_formset = self.create_formset()

        self.assertFalse(test_formset.is_valid())
        self.assertFormSetError(test_formset, field='barcode', errors='invalid lab number entered',
                                form_index=0)

    def test_invalid_one_barcode(self):
        self.data['matchpairbarcode_set-0-barcode'] = 'D24.654321'

        test_formset = self.create_formset()

        self.assertFalse(test_formset.is_valid())
        self.assertFormSetError(test_formset, field=None, errors='Must enter more than one barcode',
                                form_index=None)

    def test_invalid_gap_in_barcodes(self):
        self.data['matchpairbarcode_set-TOTAL_FORMS'] = '3'
        self.data['matchpairbarcode_set-0-barcode'] = 'D24.654321'
        self.data['matchpairbarcode_set-1-barcode'] = None
        self.data['matchpairbarcode_set-2-barcode'] = 'D24.654321'

        test_formset = self.create_formset()

        self.assertFalse(test_formset.is_valid())
        self.assertFormSetError(test_formset, field=None, errors='Cannot have a gap in the barcodes entered',
                                form_index=None)


    def test_warning_not_all_barcodes_entered(self):
        self.data['matchpairbarcode_set-TOTAL_FORMS'] = '3'
        self.data['matchpairbarcode_set-0-barcode'] = 'D24.654321'
        self.data['matchpairbarcode_set-1-barcode'] = 'D24.654321'
        self.data['matchpairbarcode_set-2-barcode'] = None

        test_formset = self.create_formset()

        self.assertTrue(test_formset.is_valid())
        self.assertIn('only 2 of 3 barcodes added', test_formset.errors )

