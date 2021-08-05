from django.contrib.auth import views as auth_views
from django.urls import path

from .views import (
    MovieDetail,
    MovieList,
    ShowAllUsers,
    movie_create,
    movie_delete,
    comments,
    show_movie,
)

app_name = 'movies'
urlpatterns = [
    path('', MovieList.as_view(), name='all_movie'),
    path('movie/<int:pk>/details/', MovieDetail.as_view(), name='detail_movie'),
    path('create_movie/', movie_create, name='create_movie'),
    path('create_movie/<int:m_id>/', movie_create, name='create_movie'),
    path('delete/<int:m_id>/movie/', movie_delete, name='delete_movie'),
    path('comments/<int:m_id>/movie/', comments, name='comments'),

    # Show users data
    path('users/', ShowAllUsers.as_view(), name='users'),

    # Test urls
    path('movie_sorted/', show_movie, name='movie_sorted'),
]
