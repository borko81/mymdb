# import django needed module's
# Import outside module
from datetime import datetime

from django.conf import settings
from django.db import models
from django.db.models import Sum, Count


class Movie(models.Model):
    """
    Store a movie info
    :Rating
    :title
    :plot
    :year
    :rating:
    :movie runtime
    :movie original url
    :movie image
    """
    NOT_RATED = 0
    RATED_R = 1
    RATED_G = 2
    RATINGS = (
        (NOT_RATED, 'Not Rated'),
        (RATED_R, 'R - Restricted'),
        (RATED_G, 'G - General Audiences')
    )

    title = models.CharField(max_length=100)
    plot = models.TextField()
    year = models.PositiveIntegerField()
    rating = models.IntegerField(
        choices=RATINGS
    )
    runtime = models.PositiveIntegerField()
    website = models.URLField(blank=True)
    image = models.ImageField(upload_to='images', blank=False)

    def __str__(self):
        return f"Title: {self.title}"


def get_max_comments():
    """Return first 2 movie with more comments"""
    return Movie.objects.all().annotate(post=Count('comments')).order_by('-post')[:4]


# UserProfile edit
class Profile(models.Model):
    """
    Extend user profile
    :onetoone for user
    :date_of_birth
    :photo for user
    """
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%M/%d', blank=True)

    def __str__(self) -> str:
        return 'Profile for user {}'.format(self.user.username)


class Comments(models.Model):
    """
    Use for comment system, add comment for user to movie
    """
    post = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    created_on = models.DateTimeField(default=datetime.now)
    author = models.CharField(max_length=50)

    class Meta:
        """Sorting movie, new is first"""
        ordering = ['-created_on']

    def __str__(self):
        return 'Comment for {}'.format(self.post.title)
