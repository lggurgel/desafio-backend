from django.urls import path
from ranking.views import UserRateMovieView, UserRankingListView, RatingDeleteView, GeneralMovieRating

urlpatterns = [
    path('create/', UserRateMovieView.as_view(), name='user-rate-movie'),
    path('list/', UserRankingListView.as_view(), name='user-rankings' ),
    path('delete/<int:pk>', RatingDeleteView.as_view(), name='delete-rating'),
    path('general-list/', GeneralMovieRating.as_view(), name='general-movie-rating')
]