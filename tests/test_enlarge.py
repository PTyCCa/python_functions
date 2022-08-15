from Challanges.enlarge import enlarge


def test_enlarge():
    assert enlarge([
        '!#',
        '$@',
    ]) == [
        '!!##',
        '!!##',
        '$$@@',
        '$$@@',
    ]