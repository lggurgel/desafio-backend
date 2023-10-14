from django.db import models
from users.models import CustomUser
from .enums import GENRE_CHOICES, SELECT


class Movie(models.Model):

    year = models.IntegerField()
    director = models.CharField(max_length=100)
    genre = models.CharField(
        max_length=100,
        choices=GENRE_CHOICES,
        default=SELECT
    )
    personal_rating = models.PositiveIntegerField(
        choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
