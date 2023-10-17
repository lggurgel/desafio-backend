from django.db import models
from users.models import CustomUser
from movies.models import Movie

class Ranking(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    personal_rating = models.PositiveIntegerField(choices=[(1,'1'), (2,'2'), (3,'3'), (4, '4'), (5, '5')], null=True)