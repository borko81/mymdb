from django.contrib import admin

from .models import Movie, Profile, Comments


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = 'title year rating runtime'.split()
    list_filter = ('year', )


admin.site.register(Profile)
admin.site.register(Comments)
