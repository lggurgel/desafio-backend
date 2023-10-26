from django.urls import path
from ranking.views import UserRateMovieView, UserRankingListView, RatingDeleteView, GeneralListMovieRatingView

urlpatterns = [
    path('rate/', UserRateMovieView.as_view(), name='user-rate-movie'),
    path('list/', UserRankingListView.as_view(), name='user-rankings' ),
    path('delete/<int:pk>', RatingDeleteView.as_view(), name='delete-rating'),
    path('general-list/', GeneralListMovieRatingView.as_view(), name='general-movie-rating')
]