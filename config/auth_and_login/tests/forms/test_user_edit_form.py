from django.contrib.auth.models import User
from django.test import TestCase

from ...forms import UserEditForm


class TestUserEditForm(TestCase):

    def test_user_edit_form_when_all_is_right_form_is_correct(self):
        form = UserEditForm(data={
            'first_name': 'borko',
            'last_name': 'alabala',
            'email': 'korea60@abv.bg'
        })
        self.assertTrue(form.is_valid())
