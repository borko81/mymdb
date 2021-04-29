from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import ListView, DetailView, CreateView
from core.models import Movie
from core.forms import NewMovieForm


def all_movie(request):
    return render(request, 'core/all_movies.html')


class MovieList(ListView):
    """ Return all movies from database """
    template_name = 'core/all_movies.html'
    model = Movie
    context_object_name = 'movies'


class MovieDetail(DetailView):
    """ Return detail from choiced movie """
    template_name = 'core/detail_movie.html'
    model = Movie
    context_object_name = 'movies'


def movie_create(request, m_id=None):
    """
        Use 2 in 1 for create and edit new movie
        for this use and two url's
    """
    context = {}
    movies = None
    if m_id:
        movies = Movie.objects.get(id=m_id)

    form = NewMovieForm(request.POST or None,
                        request.FILES or None, instance=movies)
    if form.is_valid():
        form.save()
        form = NewMovieForm()
        return redirect('movies:all_movie')
    context['form'] = form
    return render(request, 'core/new_movie.html', context)


def movie_delete(request, m_id):
    context = {}
    movie = get_object_or_404(Movie, id=m_id)
    context['movies'] = movie
    if request.method == 'POST':
        movie.delete()
        return redirect('movies:all_movie')
    return render(request, 'core/delete_movie.html', context)
