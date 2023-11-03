from django.urls import path
from movies.views import AddMovieView, MovieDetailView, UpdateMovieView, CreatedMovieListView, ListAllMovies, RecommendedMoviesView

urlpatterns = [
    path('add/', AddMovieView.as_view(), name='add-movies'),
    path('movie/<int:pk>/', MovieDetailView.as_view(), name='movie'),
    path('update/<int:pk>/', UpdateMovieView.as_view(), name='update-movies'),
    path('created/', CreatedMovieListView.as_view(), name='created-movies'),
    path('list/', ListAllMovies.as_view(), name='list-all-movies'),
    path('recommended/', RecommendedMoviesView.as_view(), name='recommended-movies')
]