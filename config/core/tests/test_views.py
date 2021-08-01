from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

from ..models import Movie


class TestMovieViews(TestCase):

    def setUp(self):
        self.client = Client()
        author = User.objects.create(username='borko')
        Movie.objects.create(
            title='Test title',
            plot='Some magic plot',
            year=1981,
            rating=1,
            runtime=120,
            website='https://google.bg',
            image='test.jpg',
            publisher=author,
        )

    def test_show_movie_get(self):
        response = self.client.get(reverse('movies:all_movie'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/all_movies.html')

    def test_movie_details(self):
        response = self.client.get(reverse('movies:detail_movie', args=[1]))
        # print(response)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/detail_movie.html')

    def test_movie_post(self):
        response = self.client.get(reverse('movies:create_movie'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/user/login/')

    def test_movie_delete(self):
        response = self.client.get(reverse('movies:delete_movie', args=[1]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/user/login/')


class TestCommentsViews(TestCase):

    def setUp(self):
        self.client = Client()
        author = User.objects.create(username='borko')
        Movie.objects.create(
            title='Test title',
            plot='Some magic plot',
            year=1981,
            rating=1,
            runtime=120,
            website='https://google.bg',
            image='test.jpg',
            publisher=author,
        )

    def test_comments_get(self):
        response = self.client.get(reverse('movies:comments', args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/comments.html')