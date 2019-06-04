import pytest

from videoclub.movies.models import Movie


@pytest.fixture
def movie():
    return Movie.objects.create(title='John Wick', price=10)
