from django.contrib import admin

from django.contrib.admin import register

from videoclub.movies.models import Movie


@register(Movie)
class MovieAdmin(admin.ModelAdmin):
    fields = ('title', 'price', 'score', 'genre',)
    list_display = ('title', 'score', 'genre',)
    list_filter = ('genre',)
    readonly_fields = ('score',)
