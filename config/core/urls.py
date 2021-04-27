from django.urls import path
from .views import testme, all_movie

urlpatterns = [
    path('', testme, name='index'),
    path('all/', all_movie, name='all_movie')
]