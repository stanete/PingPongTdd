import pytest

from videoclub.flags.models import Flag


@pytest.fixture
def flag_show_ratings_active():
    Flag.objects.filter(name='show_ratings').update(is_active=True)
