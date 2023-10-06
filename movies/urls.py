from django.urls import path
from .views import AddMovieWathcedList

urlpatterns = [
    path('add-movie/', AddMovieWathcedList.as_view(), name='add-movie')
]