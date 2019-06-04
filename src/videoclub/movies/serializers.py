from rest_framework import serializers

from videoclub.flags import flag
from videoclub.movies.models import Movie


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('title', 'price', 'score',)
        read_only_fields = ('score',)

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        if not flag.is_active('show_ratings'):
            del representation['score']

        return representation
