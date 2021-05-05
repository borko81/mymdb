from django.db import models
from django.conf import settings


class Movie(models.Model):
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


# UserPRofile edit
class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%M/%d', blank=True)

    def __str__(self) -> str:
        return 'Profile for user {}'.format(self.user.username)
