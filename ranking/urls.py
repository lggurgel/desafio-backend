from django.urls import path
from ranking.views import UserRateMovieView, UserRankingListView, RatingDeleteView, GeneralMovieRating

urlpatterns = [
    path('user-rate-movie/', UserRateMovieView.as_view(), name='user-rate-movie'),
    path('user-rankings/', UserRankingListView.as_view(), name='user=rankings' ),
    path('delete-rating/<int:pk>', RatingDeleteView.as_view(), name='delete-rating'),
    path('general-movie-rating/', GeneralMovieRating.as_view(), name='general-movie-rating')
]