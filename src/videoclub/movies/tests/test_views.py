import pytest
from rest_framework import status


@pytest.mark.django_db
class TestGetMovie:

    def test_returns_movie_when_movie_exists(self, client, movie):
        response = client.get(f'/movies/{movie.id}')

        assert response.status_code == status.HTTP_200_OK
        assert response.json() == {
            'title': 'John Wick',
            'price': '10.00',
        }
