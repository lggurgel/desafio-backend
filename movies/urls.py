from django.urls import path
from movies.views import AddMovieWathcedList, CreatedMovieListView, UpdateMovieWatched, ListAllMovies, RecommendedMoviesView

urlpatterns = [
    path('add/', AddMovieWathcedList.as_view(), name='add-movies'),
    path('created/', CreatedMovieListView.as_view(), name='created-movies'),
    path('update/<int:pk>', UpdateMovieWatched.as_view(), name='update-movies'),
    path('list/', ListAllMovies.as_view(), name='list-all-movies'),
    path('recommended/', RecommendedMoviesView.as_view(), name='recommended-movies')
]