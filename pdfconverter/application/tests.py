from django.test import TestCase, RequestFactory
from .form import UploadFileForm
from .views import pdf_converter

class url_FormTestCase(TestCase):
    ''' Basic tests to check the form validity'''
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()

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
   
    def test_getmethod(self):
        request = self.factory.get('/')
        response = pdf_converter(request)
        self.assertEqual(response.status_code, 200)
  

    def test_postmethod(self):
        request = self.factory.post('/', {"url": "http://cricinfo.com"})
        response = pdf_converter(request)
        self.assertEqual(response.status_code, 200)
        
