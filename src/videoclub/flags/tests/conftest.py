import pytest

from videoclub.flags.models import Flag


@pytest.fixture
def active_flag():
    return Flag.objects.create(name='throttling', is_active=True)


@pytest.fixture
def inactive_flag():
    return Flag.objects.create(name='anti-gravity')
