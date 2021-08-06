from django.contrib.auth.models import User
from django.test import TestCase

from ...models import Profile


class TestProfileModel(TestCase):
    def setUp(self):
        self.user_test = User.objects.create(username='borko')

    def test_create_profile(self):
        pr = Profile.objects.create(user=self.user_test, date_of_birth='1981-07-20', photo = 'myimage.jpg')
        self.assertEqual(pr.user, self.user_test)
        self.assertEqual(Profile.objects.all().count(), 1)
