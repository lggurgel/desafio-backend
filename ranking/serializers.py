from rest_framework import serializers
from ranking.models import Ranking, Comment
from movies.serializers import MovieSerializer


class UserRateMovieSerializer(serializers.ModelSerializer):

    comment = serializers.SerializerMethodField()
    movie = serializers.SerializerMethodField()

    class Meta:
        model = Ranking
        fields = ['movie', 'personal_rating', 'comment']


    def get_comment(self, obj: Ranking):
        if obj.comment:
            return CommentSerializer(obj.comment).data
        return None

    # def create(self, validated_data):
    #     request = self.context["request"]

    #     from pprint import pprint
    #     pprint(request.data)

    #     return super().create(validated_data)

    def get_movie(self, obj: Ranking):
        return MovieSerializer(instance=obj.movie).data

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

class UserRankingListSerializer(serializers.ModelSerializer):
    movie = serializers.ReadOnlyField(source='movie.title')

    class Meta:
        model = Ranking
        exclude = ('user',)

class GeneralMovieRatingSerializer(serializers.Serializer):
    movie_title = serializers.CharField()
    rating = serializers.DecimalField(max_digits=3, decimal_places=2)
