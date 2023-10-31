from django.http import Http404
from django.db.models import Avg, Q
from movies.models import Movie
from ranking.models import Ranking, Comment
from ranking.serializers import CommentSerializer

def create_ranking_instance(user, movie_id, rating, comment = None):
    try:
        movie = Movie.objects.get(pk=movie_id)
    except Movie.DoesNotExist:
        raise Http404('Movie not found')
    
    ranking_instance = Ranking.objects.filter(Q(user=user, movie=movie)).first()

    if ranking_instance:
        ranking_instance.personal_rating = rating
        if comment:
            if ranking_instance.comment:
                ranking_instance.comment.text = comment
                ranking_instance.comment.save()
            else:
                comment_instance, created = Comment.objects.get_or_create(text=comment)
                ranking_instance.comment = comment_instance
        else:
            ranking_instance.comment = None
        
        ranking_instance.save()
    
    else:
        ranking_instance = Ranking.objects.create(user=user, movie=movie, personal_rating=rating, comment=comment)


    return ranking_instance


def calculate_movie_ratings():
    movie_ratings = Ranking.objects.values('movie__title').annotate(avg_rating=Avg('personal_rating'))
    movie_ratings = movie_ratings.order_by('-avg_rating')

    return movie_ratings