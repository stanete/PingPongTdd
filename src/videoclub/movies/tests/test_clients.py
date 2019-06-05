from decimal import Decimal

import pytest
import requests

from ..clients import BadRequest, OMDBClient, Unavailable


class TestOMDBClient:

    def test_returns_movie_rating_as_decimal_when_passing_valid_title(self, responses):
        OMDBClient.API_KEY = 'my-api-key'
        request_url = 'http://www.omdbapi.com/?apikey=my-api-key&t=Die+Hard'
        responses.add(responses.GET, request_url, match_querystring=True, status=200,
                      json={'Title': 'Die Hard', 'imdbRating': '8.2'})

        rating = OMDBClient().get_rating_for_movie(title='Die Hard')

        assert rating == Decimal('8.2')

    def test_raises_unavailable_when_connection_error(self):
        with pytest.raises(Unavailable):
            OMDBClient().get_rating_for_movie(title='Die Hard')

    def test_raises_unavailable_when_request_timeout(self, responses):
        request_url = 'http://www.omdbapi.com/?apikey=my-api-key&t=Die+Hard'
        responses.add(responses.GET, request_url, match_querystring=True,
                      body=requests.Timeout())

        with pytest.raises(Unavailable):
            OMDBClient().get_rating_for_movie(title='Die Hard')

    def test_raises_bad_request_when_providing_invalid_api_key(self, responses):
        responses.add(responses.GET, 'http://www.omdbapi.com/', status=200,
                      json={'Response': False, 'Error': 'No API key provided.'})
        client = OMDBClient()
        client.API_KEY = ''

        with pytest.raises(BadRequest) as exc_info:
            client.get_rating_for_movie(title='Die Hard')

        assert exc_info.value.message == 'No API key provided.'
