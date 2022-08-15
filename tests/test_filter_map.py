from math import sqrt

from Lessons.filter_map import filter_map


def test_filter_map():
    def safe_sqrt(x):
        if x < 0:
            return False, 0
        return True, sqrt(x)

    empty = filter_map(safe_sqrt, [])
    assert not empty
    assert isinstance(empty, list)
    assert filter_map(safe_sqrt, [4, -5, -2, 9]) == [2.0, 3.0]  # noqa: WPS221
