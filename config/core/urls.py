from django.contrib.auth import views as auth_views
from django.urls import path

from .views import (
    MovieDetail,
    MovieList,
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
    # path('profile_info/<str:username>/', view_profile_info, name='profile_info'),

    # Login and register urls's
    # path('login/', user_login, name='user_login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # path('edit/', edit, name='edit'),
    # path('register/', registration, name='registration'),

    # Test urls
    path('movie_sorted/', show_movie, name='movie_sorted'),
]
