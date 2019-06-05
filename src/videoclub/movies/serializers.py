from rest_framework import serializers

from videoclub.flags import flag
from videoclub.movies.models import Movie


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('title', 'price', 'score', 'genre',)
        read_only_fields = ('score',)
        extra_kwargs = {
            'genre': {'source': 'get_genre_display'},
        }

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        if not flag.is_active('show_ratings'):
            del representation['score']

        if not representation['genre']:
            del representation['genre']

        return representation


class OMDBResponseSerializer(serializers.Serializer):
    title = serializers.CharField(source='Title', max_length=256)
    rating = serializers.DecimalField(source='imdbRating', max_digits=3, decimal_places=1)
