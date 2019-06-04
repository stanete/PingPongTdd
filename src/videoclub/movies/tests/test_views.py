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

    @pytest.mark.usefixtures('flag_show_ratings_active')
    def test_returns_movie_with_score_when_feature_flag_is_active(
            self, client, movie_with_score):
        response = client.get(f'/movies/{movie_with_score.id}')

        assert response.status_code == status.HTTP_200_OK
        assert response.json() == {
            'title': 'Die Hard',
            'price': '9.00',
            'score': 10,
        }

    def test_returns_not_found_when_movie_does_not_exist(self, client):
        response = client.get('/movies/1')

        assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.django_db
class TestListMovies:

    def test_returns_empty_list_when_no_movies_exist(self, client):
        response = client.get('/movies/')

        assert response.status_code == status.HTTP_200_OK
        assert response.json() == []

    @pytest.mark.usefixtures('movie')
    def test_returns_movies_list_when_movies_exist(self, client):
        response = client.get('/movies/')

        assert response.status_code == status.HTTP_200_OK
        assert response.json() == [{
            'title': 'John Wick',
            'price': '10.00',
        }]

    @pytest.mark.usefixtures('flag_show_ratings_active', 'movie_with_score')
    def test_returns_movies_list_with_scores_when_feature_flag_is_active(self, client):
        response = client.get(f'/movies/')

        assert response.status_code == status.HTTP_200_OK
        assert response.json() == [{
            'title': 'Die Hard',
            'price': '9.00',
            'score': 10,
        }]


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

    def test_creates_movie_with_default_score_when_score_is_passed(self, client):
        data = {
            'title': 'Top Gun',
            'price': '7.95',
            'score': 10,
        }

        response = client.post('/movies/', data)
        assert response.status_code == status.HTTP_201_CREATED
        assert Movie.objects.get(title='Top Gun', price='7.95').score == 0

    def test_returns_bad_request_when_data_without_price(self, client):
        data = {'title': 'Titanic'}

        response = client.post('/movies/', data)

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.json() == {'price': ['This field is required.']}
