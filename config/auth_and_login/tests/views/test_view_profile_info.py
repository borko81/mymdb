from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse


class TestViewProfileInfo(TestCase):
    def setUp(self):
        self.client = Client()
        self.user_for_test = User.objects.create(username='borko123', password='borko')
        self.search_user = User.objects.get(username='borko123')

    def test_show_profile(self):
        # print(self.search_user.username)
        # response = self.client.get(reverse('profile_info', args=['borko123']))
        # self.assertEqual(response.status_code, 200)
        """
            Has any error with filter, do no understand why
        """

