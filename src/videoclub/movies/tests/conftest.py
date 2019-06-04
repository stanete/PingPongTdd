import pytest

from videoclub.movies import choices
from videoclub.movies.models import Movie


@pytest.fixture
def movie():
    return Movie.objects.create(title='John Wick', price=10)


@pytest.fixture
def movie_with_score():
    return Movie.objects.create(title='Die Hard', price=9, score=10)


@pytest.fixture
def movie_with_genre():
    return Movie.objects.create(
        title='Fast and Furious', score=8, price=7, genre=choices.ACTION)
