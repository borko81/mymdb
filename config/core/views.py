from django.shortcuts import render
from django.views.generic import ListView, DetailView
from core.models import Movie


def testme(request):
    return render(request, 'base.html')


def all_movie(request):
    return render(request, 'core/all_movies.html')


class MovieList(ListView):
    template_name = 'core/all_movies.html'
    model = Movie
    context_object_name = 'movies'


class MovieDetail(DetailView):
    template_name = 'core/detail_movie.html'
    model = Movie
    context_object_name = 'movies'
