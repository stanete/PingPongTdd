from django.contrib import admin

from django.contrib.admin import register

from videoclub.movies.models import Movie


@register(Movie)
class MovieAdmin(admin.ModelAdmin):
    pass
