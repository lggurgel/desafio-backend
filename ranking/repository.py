from django.http import Http404
from django.db.models import Avg, Q
from movies.models import Movie
from ranking.models import Ranking, Comment
from ranking.serializers import CommentSerializer

def create_ranking_instance(user, movie_id, rating, comment=None):
    try:
        movie = Movie.objects.get(pk=movie_id)
    except Movie.DoesNotExist:
        raise Http404('Movie not found')
    
    ranking_instance, created = Ranking.objects.update_or_create(
        user=user,
        movie=movie,
        defaults={"personal_rating":rating},
    )

    if created:
        comment = Comment.objects.create(text=comment)
        ranking_instance.comment = comment
    else:
        if not ranking_instance.comment:
            comment_model = Comment.objects.create(text=comment) 
            ranking_instance.comment = comment_model
        else:
            ranking_instance.comment.text = comment

    ranking_instance.comment.save()
    ranking_instance.save()
    
    return ranking_instance

def calculate_movie_ratings():
    movie_ratings = Ranking.objects.values('movie__title').annotate(avg_rating=Avg('personal_rating'))
    movie_ratings = movie_ratings.order_by('-avg_rating')

    return movie_ratings