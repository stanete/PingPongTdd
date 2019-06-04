import pytest
from rest_framework import status

from videoclub.movies.models import Movie


@pytest.mark.django_db
class TestGetMovie:

    def test_returns_movie_when_movie_exists(self, client, movie):
        response = client.get(f'/movies/{movie.id}')

        assert response.status_code == status.HTTP_200_OK
        assert response.json() == {
            'title': 'John Wick',
            'price': '10.00',
        }

    def test_returns_not_found_when_movie_does_not_exist(self, client):
        response = client.get('/movies/1')

        assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.django_db
class TestCreateMovie:

    def test_creates_movie_when_data_is_valid(self, client):
        data = {
            'title': 'Top Gun',
            'price': '7.95',
        }

        response = client.post('/movies/', data)

        assert response.status_code == status.HTTP_201_CREATED
        assert Movie.objects.filter(title='Top Gun', price='7.95').exists()
