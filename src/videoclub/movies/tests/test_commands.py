import pytest
from django.core.management import call_command


@pytest.mark.django_db
class TestGenerateScoresForMovies:

    def test_generates_score_for_movie_when_score_is_zero(self, movie):
        assert movie.score == 0

        call_command('generate_scores_for_movies')

        movie.refresh_from_db()
        assert movie.score != 0

    def test_does_not_generate_score_for_movie_when_score_is_not_zero(
            self, movie_with_score):
        assert movie_with_score != 0
        expected_score = movie_with_score.score

        call_command('generate_scores_for_movies')

        movie_with_score.refresh_from_db()
        assert movie_with_score.score == expected_score
