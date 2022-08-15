from Challanges.typecheck import typecheck, typecheck_all


def test_typecheck():
    errors = []

    @typecheck(lambda *args: errors.append(args))
    def int_and_str(i: int, s: str):
        return (i, s)

    errors[:] = []  # очищаем список
    assert int_and_str(i=0, s='') == (0, '')
    assert errors == []

    errors[:] = []
    assert int_and_str(i='foo', s='bar') == ('foo', 'bar')
    assert errors == [('i', 'foo', int)]

    errors[:] = []
    assert int_and_str(i=1, s=2) == (1, 2)
    assert errors == [('s', 2, str)]


def test_typecheck_all():
    errors = []

    @typecheck_all(lambda arg: errors.append(arg))
    def int_and_str(i: int, s: str):
        return (i, s)

    assert int_and_str(i='x', s=10) == ('x', 10)
    assert errors == [
        [('i', 'x', int), ('s', 10, str)],  # один список из двух ошибок
    ]