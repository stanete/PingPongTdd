from random import randint

from django.core.management import BaseCommand

from videoclub.movies.models import Movie


class Command(BaseCommand):
    help = 'Generate random scores for movies if score is zero.'

    def handle(self, *args, **options):
        movies = Movie.objects.all()

        for movie in movies:
            if movie.score == 0:
                movie.score = randint(4, 9)
                movie.save()
