from Lessons.recursion import is_even, is_odd


def test_is_odd():
    assert not is_odd(42)
    assert is_odd(99)


def test_is_even():
    assert not is_even(99)
    assert is_even(42)