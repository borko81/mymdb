from django.db import models

# UserProfile edit
from django.conf import settings
from cloudinary import models as cloudinary_models


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
    photo = cloudinary_models.CloudinaryField(
        resource_type='image',
        blank=True
    )

    def __str__(self) -> str:
        return 'Profile for user {}'.format(self.user.username)

