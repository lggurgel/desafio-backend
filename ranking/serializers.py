from rest_framework import serializers
from ranking.models import Ranking

class UserRankMovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ranking
        exclude = ('user',)