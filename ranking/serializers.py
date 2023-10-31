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
    movie_title = serializers.CharField(source='movie.title', read_only=True)
    class Meta:
        model = Comment
        fields = ['id', 'text', 'comment_date', 'movie_title']

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

class CommentListSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)
    movie = serializers.CharField(source='movie.title', read_only=True)
    comment = serializers.CharField(source='comment.text', read_only=True)
    comment_date = serializers.DateField(source='comment.comment_date', read_only=True)

    class Meta:
        model = Ranking
        fields = ['user', 'movie', 'comment', 'comment_date']