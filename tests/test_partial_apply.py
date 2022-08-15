from operator import add, mul

from Lessons.partial_apply import flip, partial_apply


def test_partial_apply():
    assert list(
        map(partial_apply(add, 10), [1, 2, 3]),  # noqa: WPS221
    ) == [11, 12, 13]

    assert list(
        map(partial_apply(mul, '*'), [2, 3, 4]),  # noqa: WPS221
    ) == [
        '**',
        '***',
        '****',
    ]


def test_flip():
    assert flip(mul)(3, '*') == '***'


def test_both():
    assert list(
        map(partial_apply(flip(mul), 5), "!?&"),
    ) == [
        '!!!!!',
        '?????',
        '&&&&&',
    ]