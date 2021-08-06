from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

from ...models import Movie


class TestMovieViews(TestCase):

    def setUp(self):
        self.client = Client()
        author_test = User.objects.create(username='borko', password='borko')
        Movie.objects.create(
            id=1,
            title='Test title1',
            plot='Some magic plot',
            year=1981,
            rating=1,
            runtime=120,
            website='https://google.bg',
            image='test.jpg',
            publisher=author_test,
        )

    def test_show_movie_get(self):
        response = self.client.get(reverse('movies:all_movie'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/all_movies.html')

    def test_show_movie_details_when_user_is_corect_return_data(self):
        response = self.client.get(reverse('movies:detail_movie', args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Movie.objects.all()[0].plot, 'Some magic plot')
        self.assertTemplateUsed(response, 'core/detail_movie.html')

    def test_movie_post(self):
        response = self.client.get(reverse('movies:create_movie'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/user/login/')

    def test_movie_delete_when_user_is_publisher_successful_delete_movie(self):
        self.client.login(username='borko', password='borko')
        url = reverse('movies:delete_movie', kwargs={'m_id': 1})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 302)
