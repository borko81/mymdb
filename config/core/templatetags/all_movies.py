from django import template

from ..models import Movie

register = template.Library()


@register.simple_tag
def movies_count():
    """
        Return count of movie in database
    """
    return Movie.objects.all().count()
