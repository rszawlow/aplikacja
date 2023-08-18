from django.test import TestCase
from django.contrib.auth.forms import UserCreationForm  

class UserCreationFormTest(TestCase):

    def test_valid_form(self):
        form_data = {'username': 'testuser', 'password1': 'testpass123', 'password2': 'testpass123'}
        form = UserCreationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_blank_form(self):
        form = UserCreationForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 3)  # Oczekiwane 3 błędy (username, password1, password2)

