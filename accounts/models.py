from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    user_image = models.ImageField(upload_to='profile_image',
                                   blank=True, null=True)
    is_admin = models.BooleanField()

    def __str__(self):
        return self.username
