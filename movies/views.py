from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from django.http import Http404
from movies.models import Movie
from movies.serializers import MovieSerializer
from ranking.models import Ranking

class AddMovieWathcedList(CreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class UpdateMovieWatched(RetrieveUpdateAPIView):
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
    pagination_class = 2
    
    permission_classes = [AllowAny]
 
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    