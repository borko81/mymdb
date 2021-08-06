from django.contrib.auth.models import User
from django.test import TestCase

from ...forms import LoginForm


class TestLoginForm(TestCase):

    def setUp(self):
        self.test_user = User.objects.create(username='borko', password='borko')

    def test_form_login_when_data_is_ok(self):
        form = LoginForm(data={'username': self.test_user.username, 'password': self.test_user.password})
        self.assertTrue(form.is_valid())

    def test_form_login_when_data_not_ok_should_raise_error(self):
        """Empty data password"""
        form = LoginForm(data={'username': 'test'})
        self.assertFalse(form.is_valid())