from Lessons.greet import greet


def test_greet():
    try:
        greet()
    except TypeError:
        pass  # noqa: WPS420
        # thit exception is expected
    else:
        raise AssertionError('Function must not accept empty arguments!')

    assert greet('Bob') == 'Hello, Bob!'
    assert greet('Bob', 'Ann') == 'Hello, Bob and Ann!'
    assert greet('Bob', 'Ann', 'Moe') == 'Hello, Bob and Ann and Moe!'
