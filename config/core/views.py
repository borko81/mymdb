from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .forms import LoginForm, UserRegistrationForm

from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import ListView, DetailView, CreateView
from core.models import Movie, Profile
from core.forms import NewMovieForm, UserEditForm, ProfileEditForm


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

# Login and register technic


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            temp = form.cleaned_data
            user = authenticate(
                request, username=temp['username'], password=temp['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('movies:all_movie')
                else:
                    # return HttpResponse('Disabled account')
                    return redirect('movies:login')
            else:
                # return HttpResponse('Invalid login')
                return redirect('movies:login')
    else:
        form = LoginForm()
    return render(request, 'login_register/login_page.html', {'form': form})


def registration(request):
    user_form = UserRegistrationForm(request.POST or None)
    if user_form.is_valid():
        new_user = user_form.save(commit=False)
        new_user.set_password(user_form.cleaned_data['password'])
        new_user.save()
        Profile.objects.create(user=new_user)
        return render(request, 'login_register/register_done.html', {'new_user': new_user})
    return render(request, 'login_register/register.html', {'user_form': user_form})


@login_required(login_url='/login')
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(
            instance=request.user.profile, data=request.POST, files=request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('movies:all_movie')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request, 'login_register/edit_user_profile.html', {'user_form': user_form, 'profile_form': profile_form})
