from ..clients import OMDBClient


class TestOMDBClient:

    def test_returns_movie_rating_when_passing_valid_title(self, responses):
        OMDBClient.API_KEY = 'my-api-key'
        request_url = 'http://www.omdbapi.com/?apikey=my-api-key&t=Die+Hard'
        responses.add(responses.GET, request_url, match_querystring=True, status=200,
                      json={'Title': 'Die Hard', 'imdbRating': '8.2'})

        rating = OMDBClient().get_rating_for_movie(title='Die Hard')

        assert rating == '8.2'
