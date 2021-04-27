from django.shortcuts import render


def testme(request):
    return render(request, 'base.html')


def all_movie(request):
    return render(request, 'core/all_movies.html')
