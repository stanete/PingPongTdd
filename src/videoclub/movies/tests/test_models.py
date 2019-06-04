import pytest

from ..models import Movie


@pytest.mark.django_db
class TestMovie:

    def test_creates_a_movie_when_passing_title_and_price(self):
        Movie.objects.create(title='Titanic', price='3.95')

        assert Movie.objects.count() == 1

    def test_creates_a_movie_with_default_score_to_zero(self):
        Movie.objects.create(title='Titanic', price='3.95')

        movie = Movie.objects.get(title='Titanic', price='3.95')
        assert movie.score == 0

    def test_creates_a_movie_with_no_genre(self):
        Movie.objects.create(title='Titanic', price='3.95')

        movie = Movie.objects.get(title='Titanic', price='3.95')
        assert movie.genre is None
