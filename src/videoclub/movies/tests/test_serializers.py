import pytest

from ..serializers import MovieSerializer


@pytest.mark.django_db
class TestMovieSerializer:

    def test_serializes_valid_movie_with_genre(self, movie_with_score):
        serializer = MovieSerializer(movie_with_score)

        assert serializer.data == {
            'title': 'Die Hard',
            'price': '9.00',
        }

    @pytest.mark.usefixtures('flag_show_ratings_active')
    def test_serializes_score_when_flag_is_active(self, movie_with_score):
        assert movie_with_score.score == 10

        serializer = MovieSerializer(movie_with_score)

        assert serializer.data == {
            'title': 'Die Hard',
            'price': '9.00',
            'score': 10,
        }
