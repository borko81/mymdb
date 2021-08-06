from django.contrib.auth.models import User
from django.test import TestCase

from ...forms import UserRegistrationForm


class TestRegisterForm(TestCase):

    def test_form_registration_when_data_is_ok(self):
        form = UserRegistrationForm(data={
            'username': 'aladin',
            'first_name': 'borko',
            'password': 'alatest@123R',
            'password2': 'alatest@123R',
            'email': 'korea60@abv.bg'
        })
        self.assertTrue(form.is_valid())

    def test_form_registration_when_data_not_ok_should_raise_error(self):
        form = UserRegistrationForm(data={
            'username': 'aladin',
            'first_name': 'borko',
            'password': 'alatest@123R',
            'password2': 'uncorect_password',
            'email': 'korea60@abv.bg'
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {'password2': ['Password do not much']})

    def test_form_registration_username_not_allowed_should_raise_exception(self):
        form = UserRegistrationForm(data={
            'username': 'admin',
            'first_name': 'borko',
            'password': 'alatest@123R',
            'password2': 'alatest@123R',
            'email': 'korea60@abv.bg'
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {'username': ['That username not allowed']})