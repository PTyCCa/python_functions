from Lessons.updated import updated


def test_updated():
    old = {'a': 1, 'b': None, 2: 4}
    copy_of_old = old.copy()
    assert updated(old) is not old
    assert updated(old, a=2) == {'a': 2, 'b': None, 2: 4}
    assert old == copy_of_old, "Old dict should stay unchanged!"
    assert updated({}, foo='bar', bar=42) == {'foo': 'bar', 'bar': 42}
