from django.urls import path
from ranking.views import UserRateMovieView, UserRankingListView, RatingDeleteView

urlpatterns = [
    path('user-rate-movie/', UserRateMovieView.as_view(), name='user-rate-movie'),
    path('user-rankings/', UserRankingListView.as_view(), name='user=rankings' ),
    path('delete-rating/<int:pk>', RatingDeleteView.as_view(), name='delete-rating'),
]