from rest_framework.response import Response
from rest_framework import generics
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.http import Http404
from movies.models import Movie
from ranking.models import Ranking
from ranking.serializers import UserRateMovieSerializer, UserRankingListSerializer

class UserRateMovieView(CreateAPIView):
    queryset = Ranking.objects.all()
    serializer_class = UserRateMovieSerializer
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
    
class UserRankingListView(generics.ListAPIView):
    serializer_class = UserRankingListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Ranking.objects.filter(user=user).select_related('movie')