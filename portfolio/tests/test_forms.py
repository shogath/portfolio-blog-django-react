from django.test import TestCase

from portfolio.forms import ContactForm


class ContactFormTest(TestCase):
    def test_valid_form(self):
        data = {'name': 'Name', 'email': 'asd@asd.asd', 'message': 'message'}
        form = ContactForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = {'name': 'Name', 'email': 'asdasd.asd', 'message': 'message'}
        form = ContactForm(data=data)
        self.assertFalse(form.is_valid())
