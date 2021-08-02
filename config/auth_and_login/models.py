from django.db import models

# UserProfile edit
from django.conf import settings


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

