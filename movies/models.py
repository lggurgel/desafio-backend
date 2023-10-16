from django.db import models
from users.models import CustomUser
from movies.enums import GENRE_CHOICES, SELECT

class Movie(models.Model):

    title = models.CharField(max_length=100)
    year = models.IntegerField()
    director = models.CharField(max_length=100)
    genre = models.CharField(
        max_length=100,
        choices=GENRE_CHOICES,
        default=SELECT
    )
    user = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)