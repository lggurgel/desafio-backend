from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Movie
from .serializers import MovieSerializer

class AddMovieWathcedList(CreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)