from django.test import TestCase

from ...forms import ProfileEditForm


class TestUserEditForm(TestCase):

    def test_profile_edit_form_when_all_is_right_form_is_correct(self):
        form = ProfileEditForm(data={
            'date_of_birth': '1981-07-20',
            'photo': 'somecoolpicture.jpg',

        })
        print(form.errors)
        self.assertTrue(form.is_valid())

    def test_profile_edit_form_when_dateNotCorectFormat_shoudl_raise_error(self):
        """
            Think, that is not problem in form but test it.
        """
        form = ProfileEditForm(data={
            'date_of_birth': '1981/07/20',
            'photo': 'somecoolpicture.jpg',

        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['date_of_birth'], ['Enter a valid date.'])
