from rest_framework import serializers
from movies.serializers import MovieSerializer
from ranking.models import Ranking, Comment


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
    
    def get_movie(self, obj: Ranking):
        return MovieSerializer(instance=obj.movie).data

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class UserRankingListSerializer(serializers.ModelSerializer):
    movie = serializers.ReadOnlyField(source='movie.title')
    comment = serializers.ReadOnlyField(source='comment.text')

    class Meta:
        model = Ranking
        exclude = ('user',)
    
    def get_comment(self, obj):
        if obj.comment:
            return obj.comment.text
        return None

class GeneralMovieRatingSerializer(serializers.Serializer):
    movie_title = serializers.CharField()
    rating = serializers.DecimalField(max_digits=3, decimal_places=2)

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'