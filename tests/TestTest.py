import pytest


class TestTest:
    @pytest.mark.test2
    def test_some_test(self, setup):
        assert 2 == 2

    @pytest.mark.test2
    def test_some_test2(self, setup):
        assert 2 == 3