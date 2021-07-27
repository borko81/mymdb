from django.test import SimpleTestCase
from django.urls import reverse, resolve

from ..views import user_login, registration, edit


class TestLoginRegisterUrl(SimpleTestCase):

    def test_login_url(self):
        url = reverse('user_login')
        self.assertEqual(resolve(url).func, user_login)

    def test_registration_url(self):
        url = reverse('registration')
        self.assertEqual(resolve(url).func, registration)

    def test_user_edit_url(self):
        url = reverse('edit')
        self.assertEqual(resolve(url).func, edit)
