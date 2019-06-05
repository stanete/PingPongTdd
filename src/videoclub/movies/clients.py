from dataclasses import dataclass
from decimal import Decimal

import requests
from django.conf import settings

from .serializers import OMDBResponseSerializer


class OMDBClient:
    HOST_URL = 'http://www.omdbapi.com'
    API_KEY = settings.API_KEY
    DEFAULT_TIMEOUT = 5

    def get_rating_for_movie(self, title):
        try:
            response = requests.get(self.HOST_URL, params={'t': title, 'apikey': self.API_KEY},
                                    timeout=self.DEFAULT_TIMEOUT)
        except (requests.ConnectionError, requests.Timeout) as e:
            raise Unavailable() from e

        self._raise_if_error_in_response(response)

        serializer = OMDBResponseSerializer(response.json())
        movie_rating = serializer.data.get('rating')
        return Decimal(movie_rating)

    def _raise_if_error_in_response(self, response):
        error_message = response.json().get('Error')

        if error_message:
            raise BadRequest(message=error_message)


class OMDBClientException(Exception):
    pass


class Unavailable(OMDBClientException):
    pass


@dataclass
class BadRequest(OMDBClientException):
    message: str
