from rest_framework import serializers
from ranking.models import Ranking

class UserRankMovieSerializer(serializers.ModelSerializer):

    user = serializers.ReadOnlyField(source='user.id')

    class Meta:
        model = Ranking
        fields = '__all__'