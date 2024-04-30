from django.contrib.auth.models import User
from django.test import TestCase

from match_all_check.views import *
from django.urls import reverse

from django.contrib.messages import get_messages

# test views here

class BarcodecheckFormViewTest(TestCase):


    def test_get_form_class(self):
        self.user = User.objects.create_user(email="testemail1@nhs.net",
                                             first_name="test1",
                                             last_name="testington1",
                                             username='testuser1',
                                             password='12345')
        self.client.login(username='testuser1', password='12345')
        #v = self.create_Match_all_checkCreateView()
        url = reverse('match_all_check', kwargs={'barcode_count': 2})
        resp = self.client.get(url, follow=True)
        print(resp.templates)

       # print(type(v))
        self.assertTemplateUsed(resp, 'match_all_check/match_all_check.html')
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(resp.headers.get('location'), 'http://127.0.0.1:8000/match_all_check/2/')
        management_form = resp.context['form'].management_form
        self.assertEqual(management_form['TOTAL_FORMS'].value(), 2)

    def test_form_invalid(self):
        url = reverse('match_all_check', kwargs={'barcode_count': 2})
        resp = self.client.get(url)
        management_form = resp.context['form'].management_
        data ={}
        for i in range(management_form['TOTAL_FORMS'].value()):
            current_form = resp.context['form'].forms[i]
            for field_name in current_form.fields:
                value = current_form[field_name].value()
                data['%s-%s' % (current_form.prefix, field_name)] = value if value is not None else 'D24.123456'
        data['worksheet'] ='1234567'
        response = self.client.post(url, data, follow=True)
        print(data)

        #messages = [m for m in get_messages(response.wsgi_request)]
        #print( response.content.decode())
        #self.assertInHTML('Invalid Worksheet', response.content.decode())
        self.assertTemplateUsed(response, 'match_all_check/match_all_check.html')
        self.assertEqual(response.status_code, 302)




    def test_form_valid(self):
        url = reverse('match_all_check', kwargs={'barcode_count': 2})
        resp = self.client.get(url)
        management_form = resp.context['form'].management_form
        data = {}
        for i in range(management_form['TOTAL_FORMS'].value()):
            current_form = resp.context['form'].forms[i]
            for field_name in current_form.fields:
                value = current_form[field_name].value()
                data['%s-%s' % (current_form.prefix, field_name)] = value if value is not None else 'D24.123456'
        data['worksheet'] = '123456'
        response = self.client.post(url, data, follow=True)
