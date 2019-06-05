import requests
from django.conf import settings


class OMDBClient:
    HOST_URL = 'http://www.omdbapi.com'
    API_KEY = settings.API_KEY

    def get_rating_for_movie(self, title):
        response = requests.get(self.HOST_URL, params={'t': title, 'apikey': self.API_KEY})
        return response.json().get('imdbRating')
