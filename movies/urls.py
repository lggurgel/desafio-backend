from django.urls import path
from .views import AddMovieWathcedList, CreatedMovieListView, UpdateMovieWatched, ListAllMovies

urlpatterns = [
    path('add/', AddMovieWathcedList.as_view(), name='add-movies'),
    path('created/', CreatedMovieListView.as_view(), name='created-movies'),
    path('update/<int:pk>', UpdateMovieWatched.as_view(), name='update-movies'),
    path('list/', ListAllMovies.as_view(), name='list-all-movies')
]