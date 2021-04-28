from django.urls import path
from .views import (
    all_movie,
    MovieList,
)
app_name = 'movies'
urlpatterns = [
    path('', MovieList.as_view(), name='all_movie'),
    path('all/', all_movie, name='index')
]