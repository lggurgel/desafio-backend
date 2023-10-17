from django.urls import path
from ranking.views import UserRateMovieView, UserRankingListView

urlpatterns = [
    path('user-rate-movie/', UserRateMovieView.as_view(), name='user-rate-movie'),
    path('user-rankings/', UserRankingListView.as_view(), name='user=rankings' )
]