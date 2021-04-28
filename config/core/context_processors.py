from .models import Movie


def categories(request):
    return {
        'categories': Movie.objects.all()
    }
