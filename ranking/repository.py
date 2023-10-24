from ranking.models import Ranking
from movies.models import Movie
from django.http import Http404
from django.db.models import Avg


def create_ranking_instance(user, movie_id, rating):
    try:
        movie = Movie.objects.get(pk=movie_id)
    except Movie.DoesNotExist:
        raise Http404('Movie not found')

    ranking_instance, created = Ranking.objects.get_or_create(user=user, movie=movie)
    ranking_instance.personal_rating = rating
    ranking_instance.save()

    return ranking_instance


# def calculate_movie_ratings():
#     movie_ratings = Ranking.objects.values('movie__title').annotate(avg_rating=Avg('personal_rating'))
#     movie_ratings = movie_ratings.order_by('-avg_rating')

#     return movie_ratings

def calculate_movie_ratings(include_title_genre=False):
    # fields = ['movie__title', 'avg_rating']

    if include_title_genre:
        # fields.append('movie__genre')
        movie_ratings = (
        Ranking.objects
        .values('movie__title', 'movie__genre')
        .annotate(avg_rating=Avg('personal_rating'))
        .order_by('-avg_rating')
    )
        return movie_ratings

    else:
        movie_ratings = Ranking.objects.values('movie__title').annotate(avg_rating=Avg('personal_rating'))
        movie_ratings = movie_ratings.order_by('-avg_rating')

        return movie_ratings
