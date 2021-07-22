from django.contrib.auth import views as auth_views
from django.urls import path

from .views import user_login, edit, registration, view_profile_info

urlpatterns = [
    path('login/', user_login, name='user_login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('edit/', edit, name='edit'),
    path('register/', registration, name='registration'),
    path('profile_info/<str:username>/', view_profile_info, name='profile_info'),
]
