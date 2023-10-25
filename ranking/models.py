from django.db import models
from users.models import CustomUser
from movies.models import Movie

class Comment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    text = models.TextField(max_length=300)
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.movie.title}'

class Ranking(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    personal_rating = models.PositiveIntegerField(choices=[(1,'1'), (2,'2'), (3,'3'), (4, '4'), (5, '5')], null=True)
    comment = models.ForeignKey(Comment, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.user.username} - {self.movie.title}'
