from django.contrib.auth.models import AbstractUser,User
from django.db import models


class CustomUser(AbstractUser):
    user_image = models.ImageField(upload_to='profile_image',blank=True,null=True)

    def __str__(self):
        return self.username