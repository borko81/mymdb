from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase

from ..forms import NewMovieForm, CommentsForm
from ..models import Movie

testfile = (
    b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x00\x00\x00\x21\xf9\x04'
    b'\x01\x0a\x00\x01\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02'
    b'\x02\x4c\x01\x00\x3b')


class NewMovieFormTestCase(TestCase):
    """
        Test with image, not correct, I do not know how to fix!
    """

    def test_form_validation(self):
        form = NewMovieForm(data={'title': 'New title'})
        self.assertFalse(form.is_valid())

    def test_form_with_all_arguments(self):
        avatar = SimpleUploadedFile('small.jpg', testfile, content_type='images/gif')
        form_ok = NewMovieForm(
            data={'title': 'New title', 'plot': 'one', 'year': '1981', 'rating': 0, 'runtime': '60',
                  'website': 'https://google.bg', 'image': avatar})
        self.assertEqual(form_ok.errors['image'], ['This field is required.'])


class CommentsTestCase(TestCase):
    def test_comments_form_is_invalid_when_something_is_missing(self):
        form = CommentsForm(data={'post': 'one'})
        self.assertFalse(form.is_valid())

    def test_comments_form_is_valid(self):
        author = User.objects.create(username='borko')
        m = Movie.objects.create(
            title='Test title',
            plot='Some magic plot',
            year=1981,
            rating=1,
            runtime=120,
            website='https://google.bg',
            publisher=author,
        )
        form = CommentsForm(data={'post': m, 'body': 'Super', 'author': author})
        print(form.errors)
        self.assertTrue(form.is_valid())