from rest_framework.response import Response
from rest_framework import generics
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from ranking.models import Ranking
from ranking.serializers import UserRateMovieSerializer, UserRankingListSerializer
from ranking.repository import create_ranking_instance

class UserRateMovieView(CreateAPIView):
    queryset = Ranking.objects.all()
    serializer_class = UserRateMovieSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = request.user
        movie_id = request.data.get('movie')
        rating = int(request.data.get('personal_rating'))

        ranking_instance = create_ranking_instance(user, movie_id, rating)

        return Response({'message': 'Rating registered successfully!'}, status=status.HTTP_201_CREATED)
    
class UserRankingListView(generics.ListAPIView):
    serializer_class = UserRankingListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Ranking.objects.filter(user=user).select_related('movie')
    
class RatingDeleteView(generics.DestroyAPIView):
    queryset = Ranking.objects.all()
    serializer_class = UserRateMovieSerializer
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response({'message':'Rating successfully deleted.'})
        except Ranking.DoesNotExist:
            return Response({'message':'Rating not found.'})