from django.urls import path
from .views import (
    MovieDetail,
    MovieList,
)
app_name = 'movies'
urlpatterns = [
    path('', MovieList.as_view(), name='all_movie'),
    path('movie/<int:pk>/details/', MovieDetail.as_view(), name='detail_movie'),
]
