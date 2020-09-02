from django.test import TestCase

from .form import TestForm


class FormTest(TestCase):
    def test_form_valid(self):
        form = TestForm()
        self.assertEqual(len(form.fields.keys()), 9)
