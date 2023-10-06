from django.urls import path
from .views import AddMovieWathcedList, WatchedMovieListView, UpdateMovieWatched

urlpatterns = [
    path('add-movies/', AddMovieWathcedList.as_view(), name='add-movie'),
    path('watched-movies/', WatchedMovieListView.as_view(), name='watched-movies'),
    path('update-movies/<int:pk>', UpdateMovieWatched.as_view(), name='update-movies')
]