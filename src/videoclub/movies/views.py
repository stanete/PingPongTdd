from rest_framework import mixins, viewsets

from videoclub.movies.models import Movie
from videoclub.movies.serializers import MovieSerializer


class MoviesView(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
