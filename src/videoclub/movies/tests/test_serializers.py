import pytest

from ..serializers import MovieSerializer


@pytest.mark.django_db
class TestMovieSerializer:

    def test_serializes_valid_movie_with_genre(self, movie_with_genre):
        assert movie_with_genre.score == 8

        serializer = MovieSerializer(movie_with_genre)

        assert serializer.data == {
            'title': 'Fast and Furious',
            'price': '7.00',
            'genre': 'Action',
        }

    @pytest.mark.usefixtures('flag_show_ratings_active')
    def test_serializes_score_when_flag_is_active(self, movie_with_genre):
        assert movie_with_genre.score == 8

        serializer = MovieSerializer(movie_with_genre)

        assert serializer.data == {
            'title': 'Fast and Furious',
            'price': '7.00',
            'score': 8,
            'genre': 'Action',
        }

    def test_does_not_serialize_genre_when_movie_genre_is_null(self, movie):
        assert movie.genre is None

        serializer = MovieSerializer(movie)

        assert 'genre' not in serializer.data
