import pytest

from videoclub.flags import flag


@pytest.mark.django_db
class TestFlagActivation:

    def test_returns_true_when_flag_is_active(self, active_flag):
        assert flag.is_active(active_flag.name) is True

    def test_returns_false_when_flag_is_inactive(self, inactive_flag):
        assert flag.is_active(inactive_flag.name) is False

    def test_returns_false_when_flag_does_not_exist(self):
        assert flag.is_active('imaginary-feature') is False
