from django.test import TestCase
from application.form import UploadFileForm

class url_FormTestCase(TestCase):
    def test_valid_form(self):
        data = {'url':'http://www.google.com'}
        form = UploadFileForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = {
            'url': 'Some fake url',
        }
        form = UploadFileForm(data=data)
        self.assertFalse(form.is_valid())
