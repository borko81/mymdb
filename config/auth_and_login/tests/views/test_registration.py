from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse


class TestRegistrationView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_user_post_registration(self):
        response = self.client.post(
            reverse('registration'),
            data={'username': 'borko1', 'first_name': 'Boris', 'email': 'korea60@abv.bg', 'password': 'B@rko@123A',
                  'password2': 'B@rko@123A'}
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login_register/register_done.html')
        self.assertEqual(User.objects.all().count(), 1)

    def test_user_create_with_not_correct_password_should_raise_exception(self):
        response = self.client.post(
            reverse('registration'),
            data={'username': 'borko1', 'first_name': 'Boris', 'email': 'korea60@abv.bg', 'password': 'B@rko@123A',
                  'password2': 'B13'}
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login_register/register.html')
        self.assertEqual(User.objects.all().count(), 0)
