from django_filters.rest_framework import DjangoFilterBackend
from django.http import Http404
from django.db.models import Q, Avg
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from movies.models import Movie
from movies.serializers import MovieSerializer, RecommendedMovieSerializer
from ranking.models import Ranking
from ranking.repository import calculate_movie_ratings

class MyCustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 50

class AddMovieView(CreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class MovieDetailView(RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class UpdateMovieView(RetrieveUpdateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAdminUser]

    def get_object(self):
        movie_pk = self.kwargs.get('pk')
        movie = Movie.objects.filter(pk=movie_pk).first()

        if not movie:
            raise Http404
        return movie 

class CreatedMovieListView(ListAPIView): #filmes que user adicionou
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Movie.objects.filter(user=self.request.user)

class ListAllMovies(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['title', 'director']
    filterset_fields = ['genre']
    pagination_class = MyCustomPagination
    
    permission_classes = [AllowAny]
 
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
        
class RecommendedMoviesView(generics.ListAPIView):
    serializer_class = RecommendedMovieSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        user_favorite_genre = user.favorite_film_genre

        recommended_movies = (
            Movie.objects
            .filter(genre=user_favorite_genre)
            .exclude(ranking__user=user)
            .annotate(rating=Avg('ranking__personal_rating'))
            .values('title', 'rating', 'genre')
            .order_by('-rating')
        )
        return recommended_movies