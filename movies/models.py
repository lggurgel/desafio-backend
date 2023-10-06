from django.db import models
from users.models import CustomUser

class Movie(models.Model):
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

    title = models.CharField(max_length=100)
    year = models.IntegerField()
    director = models.CharField(max_length=100)
    genre = models.CharField(
        max_length=100,
        choices=GENRE_CHOICES,
        default=SELECT
    )
    personal_rating = models.PositiveIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
