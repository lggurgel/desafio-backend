from rest_framework import serializers
from ranking.models import Ranking


class UserRateMovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ranking
        exclude = ('user',)


class UserRankingListSerializer(serializers.ModelSerializer):
    movie = serializers.ReadOnlyField(source='movie.title')

    class Meta:
        model = Ranking
        exclude = ('id', 'user',)
