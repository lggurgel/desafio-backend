from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    location = models.CharField(max_length=30, null=False)

    SELECT = 'Select Genre'
    ACTION = 'Action'
    COMEDY = 'Comedy'
    DRAMA = 'Drama'
    ROMANCE = 'Romance'
    SCIFI = 'Science Fiction'
    HORROR = 'Horror'

    GENRE_CHOICES = [
        (SELECT, 'Select Genre'),
        (ACTION, 'Action'),
        (COMEDY, 'Comedy'),
        (DRAMA, 'Drama'),
        (ROMANCE, 'Romance'),
        (SCIFI, 'Science Fiction'),
        (HORROR, 'Horror'),
    ]

    favorite_film_genre = models.CharField(
        max_length=100,
        choices=GENRE_CHOICES,
        default=SELECT
    )

    def __str__(self):
        return self.username
