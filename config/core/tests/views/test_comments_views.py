from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

from ...models import Movie, Comments


class TestCommentsViews(TestCase):
    """
        Post create on SetUp
    """

    def setUp(self):
        self.client = Client()
        author_one = User.objects.create(username='borko', password='borko')
        m = Movie.objects.create(
            title='Test title',
            plot='Some magic plot',
            year=1981,
            rating=1,
            runtime=120,
            website='https://google.bg',
            image='test.jpg',
            publisher=author_one,
        )
        Comments.objects.create(post=Movie.objects.get(id=m.id), body='some body', author=author_one)

    def test_comments_get(self):
        response = self.client.get(reverse('movies:comments', args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Comments.objects.all().count(), 1)

