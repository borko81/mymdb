from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from .models import Profile


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
                    messages.success(request, 'Login successful, welcome {}'.format(user))
                    return redirect('movies:all_movie')
                else:
                    # return HttpResponse('Disabled account')
                    return redirect('user_login')
            else:
                # return HttpResponse('Invalid login')
                messages.success(request, 'Invalid login, try again')
                return redirect('user_login')
    else:
        form = LoginForm()
    return render(request, 'login_register/login_page.html', {'form': form})


def registration(request):
    """
        Register view.
        After successfully create user, too create profile, this profile used to
        attach info to user profile!
    """
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
    """
    Edit user profile
    """
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
    return render(request, 'login_register/edit_user_profile.html',
                  {'user_form': user_form, 'profile_form': profile_form})


def view_profile_info(request, username):
    """
        Return data from user profile
    """
    # search_user = User.objects.get(username=username)
    search_user = get_object_or_404(User, username=username)
    context = {}
    context['username'] = username
    # Need to check if user is super user, is it not show information about his user
    if search_user.is_superuser:
        context['info'] = 'super user'

    else:
        profiles = Profile.objects.filter(user=search_user)
        context['info'] = profiles[0]
    return render(request, 'login_register/profile_view.html', context)
