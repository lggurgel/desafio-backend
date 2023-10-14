from django.urls import path
from ranking.views import UserRankMovieView

urlpatterns = [
    path('user-rank-movie/', UserRankMovieView.as_view(), name='user-rank-movie')
]