from rest_framework import serializers
from ranking.models import Ranking


class UserRateMovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ranking
        fields = ['movie', 'personal_rating', 'comment']


class UserRankingListSerializer(serializers.ModelSerializer):
    movie = serializers.ReadOnlyField(source='movie.title')

    class Meta:
        model = Ranking
        exclude = ('user',)

class GeneralMovieRatingSerializer(serializers.Serializer):
    movie_title = serializers.CharField()
    rating = serializers.DecimalField(max_digits=3, decimal_places=2)