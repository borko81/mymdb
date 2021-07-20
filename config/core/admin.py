from django.contrib import admin

from .models import Movie, Profile, Comments


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = 'title year rating runtime'.split()
    list_filter = ('year',)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = 'user date_of_birth'.split()
    list_filter = ('user',)
    search_fields = ('user', )


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = 'post author created_on'.split()
    search_fields = ('author', )
    list_filter = ('author',)
