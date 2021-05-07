from django.test import SimpleTestCase
from django.urls import reverse, resolve
from django.contrib.auth import views as auth_views
from core.views import (
    MovieList,
    MovieDetail,
    movie_create,
    movie_delete,
    user_login,
    registration,
    edit,
)

# py manage.py test core/tests


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


class TestLoginRegisterUrl(SimpleTestCase):

    def test_login_url(self):
        url = reverse('movies:user_login')
        self.assertEqual(resolve(url).func, user_login)

    def test_logout_url(self):
        url = reverse("movies:logout")
        self.assertEqual(resolve(url).func.view_class, auth_views.LogoutView)

    def test_registration_url(self):
        url = reverse('movies:registration')
        self.assertEqual(resolve(url).func, registration)

    def test_user_edit_url(self):
        url = reverse('movies:edit')
        self.assertEqual(resolve(url).func, edit)
