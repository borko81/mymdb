from django.test import SimpleTestCase
from django.urls import reverse, resolve

# py manage.py test core/tests
from ..views import MovieList, MovieDetail, movie_create, movie_delete


class TestUrls(SimpleTestCase):

    def test_all_movie_url(self):
        url = reverse('movies:all_movie')
        # print(resolve(url))
        self.assertEqual(resolve(url).func.view_class, MovieList)

    def test_movie_detail(self):
        url = reverse('movies:detail_movie', args=['1'])
        self.assertEqual(resolve(url).func.view_class, MovieDetail)

    def test_movie_create(self):
        url = reverse('movies:create_movie')
        self.assertEqual(resolve(url).func, movie_create)

    def test_movie_create_with_param(self):
        url = reverse('movies:create_movie', args=['1'])
        self.assertEqual(resolve(url).func, movie_create)

    def test_movie_delete(self):
        url = reverse('movies:delete_movie', args=['1'])
        self.assertEqual(resolve(url).func, movie_delete)
