from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from django.http import Http404
from movies.models import Movie
from movies.serializers import MovieSerializer

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
        movie = Movie.objects.filter(pk=movie_pk, user=self.request.user).first()

        if not movie:
            raise Http404
        return movie 

class WatchedMovieListView(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Movie.objects.filter(user=self.request.user)

class ListAllMovies(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [AllowAny]
 
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)