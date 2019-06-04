import pytest

from videoclub.movies.models import Movie


@pytest.fixture
def movie():
    return Movie.objects.create(title='John Wick', price=10)


@pytest.fixture
def movie_with_score():
    return Movie.objects.create(title='Die Hard', price=9, score=10)
