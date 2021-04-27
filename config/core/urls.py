from django.urls import path
from .views import testme

urlpatterns = [
    path('', testme, name='index')
]