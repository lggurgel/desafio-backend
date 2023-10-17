from ranking.models import Ranking
from movies.models import Movie
from django.http import Http404

def create_ranking_instance(user, movie_id, rating):
    try:
        movie = Movie.objects.get(pk=movie_id)
    except Movie.DoesNotExist:
        raise Http404('Movie not found')
    
    ranking_instance, created = Ranking.objects.get_or_create(user=user, movie=movie)
    ranking_instance.personal_rating = rating
    ranking_instance.save()

    return ranking_instance