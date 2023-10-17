from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.http import Http404
from movies.models import Movie
from ranking.models import Ranking
from ranking.serializers import UserRankMovieSerializer

class UserRankMovieView(CreateAPIView):
    queryset = Ranking.objects.all()
    serializer_class = UserRankMovieSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        movie_id = request.data.get('movie')
        ranking = int(request.data.get('personal_rating'))

        try:
            movie = Movie.objects.get(pk=movie_id)
        except Movie.DoesNotExist:
            raise Http404('Filme não encontrado')
        
        user = request.user

        ranking_instance, created = Ranking.objects.get_or_create(user=user, movie=movie)
        ranking_instance.personal_rating = ranking
        ranking_instance.save()

        return Response({'message': 'Avaliação registrada com sucesso!'}, status=status.HTTP_201_CREATED)
    
    