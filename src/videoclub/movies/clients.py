from decimal import Decimal

import requests
from django.conf import settings

from .serializers import OMDBResponseSerializer


class OMDBClient:
    HOST_URL = 'http://www.omdbapi.com'
    API_KEY = settings.API_KEY

    def get_rating_for_movie(self, title):
        response = requests.get(self.HOST_URL, params={'t': title, 'apikey': self.API_KEY})
        serializer = OMDBResponseSerializer(response.json())

        movie_rating = serializer.data.get('rating')
        return Decimal(movie_rating)
