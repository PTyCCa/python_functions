from Lessons.keep_truthful import abs_sum, keep_truthful, walk

FALSES = (False, (), None, '', 0)
TRUTHS = (True, (1,), '!', -5)


def test_keep_truthful():
    assert list(keep_truthful(FALSES)) == [], (
        'All falsy values sholud be filtered out!'
    )
    assert list(keep_truthful(TRUTHS)) == list(TRUTHS), (
        'All truthful values sholud be keeped!'
    )
    assert list(keep_truthful([0, 1, 0])) == [1]


def test_abs_sum():
    assert abs_sum([0]) == 0
    assert abs_sum((-42,)) == 42
    assert abs_sum([-3, -2, -1, 0, 1, 2, 3]) == 12  # noqa: WPS221


def test_walk():
    city = {
        'Pine': {
            '5': 'School #42',
        },
        'Elm': {
            '13': {
                '1': 'Appartments #2, Elm st.13',
            },
        },
    }
    assert walk(city, ['Pine', '5']) == city['Pine']['5']
    path = ['Elm', '13', '1']
    assert walk(city, path) == city['Elm']['13']['1']