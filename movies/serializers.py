from rest_framework import serializers
from movies.models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        exclude = ('user'),

class RecommendedMovieSerializer(serializers.Serializer):
    movie_title = serializers.CharField()
    avg_rating = serializers.DecimalField(max_digits=3, decimal_places=2)
    
    class Meta:
        fields = '__all__'