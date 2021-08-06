from django.contrib.auth.models import User
from django.test import TestCase

from ...models import Movie, Comments


class MovieTestCase(TestCase):
    def setUp(self):
        author = User.objects.create(username='borko')
        Movie.objects.create(
            title='Test title',
            plot='Some magic plot',
            year=1981,
            rating=1,
            runtime=120,
            website='https://google.bg',
            publisher=author,
        )

    def test_movie_is_ok_or_not(self):
        movie_test = Movie.objects.get(title='Test title')
        self.assertEqual(movie_test.year, 1981)
        self.assertEqual(movie_test.rating, 1)


class CommentsTestCase(TestCase):
    def setUp(self):
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
        Comments.objects.create(
            post=m,
            body='comments for first post',
            author='borko'
        )

    def test_comments_is_created_or_not(self):
        comments_for_test = Comments.objects.get(id=1)
        self.assertEqual(comments_for_test.author, 'borko')
