from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import ListView, DetailView

from .forms import CommentsForm
from .forms import NewMovieForm
from .models import Comments, get_max_comments
from .models import Movie


def show_movie(request):
    """
        Return most comments movies
    """
    movie_with_more_comments = get_max_comments()
    context = {
        'data': movie_with_more_comments
    }

    return render(request, 'core/sort_moview_list.html', context)


class MovieList(ListView):
    """ Return all movies from database """
    template_name = 'core/all_movies.html'
    model = Movie
    context_object_name = 'movies'
    paginate_by = 4


class MovieDetail(DetailView):
    """ Return detail from choice movie """
    template_name = 'core/detail_movie.html'
    model = Movie
    context_object_name = 'movies'


def movie_create(request, m_id=None):
    """
        Use 2 in 1 for create and edit new movie
        for this use and two url's
    """
    if request.user.is_authenticated:
        """
            If user is login get control for create, delete and edit
            else redirect to login page
        """
        context = {}
        movies = None
        if m_id:
            movies = Movie.objects.get(id=m_id)

        form = NewMovieForm(request.POST or None,
                            request.FILES or None, instance=movies)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.publisher = request.user
            movie.save()
            form = NewMovieForm()
            return redirect('movies:all_movie')
        context['form'] = form
        return render(request, 'core/new_movie.html', context)
    return redirect('user_login')


def movie_delete(request, m_id):
    if request.user.is_authenticated:
        context = {}
        movie = get_object_or_404(Movie, id=m_id)
        context['movies'] = movie
        if request.method == 'POST':
            movie.delete()
            return redirect('movies:all_movie')
        return render(request, 'core/delete_movie.html', context)
    return redirect('user_login')


def comments(request, m_id):
    """
    Add comments to movie, show only date and body message
    Logic to view and add new comment is move to tempalte
    """
    # if request.user.is_authenticated:
    context = {}
    movie = get_object_or_404(Movie, id=m_id)
    movie_comments = Comments.objects.filter(post=movie)
    context['movies'] = movie
    context['comments'] = movie_comments
    context['form'] = CommentsForm()
    if request.method == 'GET':
        return render(request, 'core/comments.html', context)
    movie_id = request.POST['movie_id']
    movie_body = request.POST['movie_body']
    Comments.objects.create(post=Movie.objects.get(id=movie_id), body=movie_body, author=request.user)
    return redirect('movies:comments', m_id)
    # return redirect('movies:user_login')


class ShowAllUsers(LoginRequiredMixin, ListView):
    template_name = 'core/show_all_users.html'
    context_object_name = 'persons'
    model = User
