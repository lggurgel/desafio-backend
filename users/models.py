from django.db import models
from django.contrib.auth.models import AbstractUser
from movies.enums import GENRE_CHOICES, SELECT


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    location = models.CharField(max_length=30, null=False)
    favorite_film_genre = models.CharField(
        max_length=100,
        choices=GENRE_CHOICES,
        default=SELECT
    )

    def __str__(self):
        return self.username
