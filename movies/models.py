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
    
    # Remover esse campo
    # The relation between User and Movie would be through Rating
    
    # Some of the Rating fields
    # Don't rank a movie twice
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    personal_rating = models.PositiveIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])
    description = models.TextField()

    # Criar o modelo Ranking
    # Criar uma view para registrar o Rank do User com Movie (receber id do filme e id do user)
    # Criar uma view para listar os personal rankings
    # Criar uma view para fazer upade do ranking
    # Criar uma view para deletar o ranking